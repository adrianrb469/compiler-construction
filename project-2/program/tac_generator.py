import inspect
import sys

sys.path.append("..")
from typing import List, Optional

from antlr4 import *
from utils.utils import arithmetic_op, getDeclType, types_comparable

from .CompiscriptLexer import CompiscriptLexer
from .CompiscriptParser import CompiscriptParser
from .CompiscriptVisitor import CompiscriptVisitor
from .SymbolTable import (
    ClassSymbol,
    DataType,
    FunctionSymbol,
    Symbol,
    SymbolTable,
    SymbolType,
    UnionType,
)

from .tac import IntermediateCodeGenerator, Operation


class CompiscriptCompiler(CompiscriptVisitor):
    def __init__(self) -> None:
        self.code_generator = IntermediateCodeGenerator()
        self.current_function: Optional[str] = None
        self.function_params: List[str] = []

    def visit(self, tree):
        if tree is None:
            print("Error: Attempting to visit None")
            return None
        try:
            return super().visit(tree)
        except Exception as e:
            # Include line and column for better error localization
            if hasattr(tree, "start"):
                line = tree.start.line
                column = tree.start.column
                current_function = inspect.stack()[1].function
                print(
                    f"Error during visit in {current_function}: {e} at {line}:{column}"
                )
            else:
                print(f"Error during visit: {e}")
            return None

    def visitProgram(self, ctx: CompiscriptParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visit(declaration)
        # After visiting all declarations, return the generated code
        return self.code_generator.get_code()

    # declaration: classDecl | funDecl | varDecl | statement;
    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        return self.visitChildren(ctx)

    # classDecl: 'class' IDENTIFIER ('extends' IDENTIFIER)? '{' functions '}';
    def visitClassDecl(self, ctx: CompiscriptParser.ClassDeclContext):
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visit(ctx.function())

    # INDENTIFIER '(' parameters? ')' block
    def visitFunction(self, ctx: CompiscriptParser.FunctionContext):
        function_name = ctx.IDENTIFIER().getText()
        self.current_function = function_name
        self.function_params = []

        # Emit the label for the function
        self.code_generator.emit(Operation.LABEL, result=function_name)

        # If there are parameters, visit them
        if ctx.parameters():
            for param in ctx.parameters().IDENTIFIER():
                param_name = param.getText()
                self.function_params.append(param_name)
                # Emit the parameter declaration
                self.code_generator.emit(Operation.PARAM, result=param_name)

        # Visit the function block
        self.visit(ctx.block())

        # If there's no return statement, add a default return
        # self.code_generator.emit(Operation.RETURN)

        self.current_function = None

        return function_name

    # varDecl: 'var' IDENTIFIER ('=' expression)? ';'
    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):
        var_name = ctx.IDENTIFIER().getText()
        if ctx.expression():
            # Evaluate the initializer expression
            expr_result = self.visit(ctx.expression())
            # Assign the result to the variable
            self.code_generator.emit(
                op=Operation.ASSIGN, arg1=expr_result, result=var_name
            )
        else:
            # No initializer; assign a default value (e.g., 0)
            self.code_generator.emit(op=Operation.ASSIGN, arg1="0", result=var_name)
        return var_name

    def visitStatement(self, ctx: CompiscriptParser.StatementContext):
        return self.visitChildren(ctx)

    def visitExprStmt(self, ctx: CompiscriptParser.ExprStmtContext):
        # Evaluate the expression statement
        self.visit(ctx.expression())
        return None

    def visitForStmt(self, ctx: CompiscriptParser.ForStmtContext):
        # evaluate if there is an initialization of varDecl
        if ctx.varDecl():
            # evaluate the iniialization of varDecl
            var_name = self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            # evaluate the assignment
            var_name = self.visit(ctx.exprStmt())

        # generate the for label to return to the start of the loop
        for_label = self.code_generator.new_label()
        # generate the break label for breaking out of the loop
        break_label = self.code_generator.new_label()
        # emit the for label
        self.code_generator.emit(Operation.LABEL, result=for_label)
        # get the expression type by visiting the expression
        condition = self.visit(ctx.expression(0))
        # generate the if_false instruction to break out of the loop
        self.code_generator.emit(
            Operation.IF_FALSE, arg1=condition, arg2="GOTO", result=break_label
        )
        # visit the block of code
        self.visit(ctx.statement())
        # evaluate the increment or decrement expression
        expression = ctx.expression(1).getText()
        # generate a new temporary variable for the result
        temp = self.code_generator.new_temp()
        operation = None
        number = 0

        if "+=" in expression:
            operation = Operation.ADD
            number = expression.split("+=")[1]
        elif "-=" in expression:
            operation = Operation.SUB
            number = expression.split("-=")[1]
        elif "++" in expression:
            operation = Operation.ADD
            number = 1
        elif "--" in expression:
            operation = Operation.SUB
            number = 1

        # emit increment or decrement instruction
        self.code_generator.emit(operation, arg1=var_name, arg2=number, result=temp)
        # assign the result to the variable
        self.code_generator.emit(Operation.ASSIGN, arg1=temp, result=var_name)

        # emit the goto instruction to return to the start of the loop
        self.code_generator.emit(Operation.GOTO, result=for_label)
        # emit the label for the break
        self.code_generator.emit(Operation.LABEL, result=break_label)

        return None

    def visitIfStmt(self, ctx: CompiscriptParser.IfStmtContext):
        # Evaluate the condition expression and get its temporary result
        condition = self.visit(ctx.expression())

        # Generate unique labels for else branch and end of if
        label_else = self.code_generator.new_label()

        # Only create label_end if there's an else block
        label_end = self.code_generator.new_label() if ctx.statement(1) else None

        # Emit IF_FALSE condition GOTO label_else
        self.code_generator.emit(
            Operation.IF_FALSE, arg1=condition, arg2="GOTO", result=label_else
        )

        # Visit the 'then' statement
        self.visit(ctx.statement(0))

        # If there's an else block, emit GOTO to skip over it and define label_end
        if label_end:
            self.code_generator.emit(Operation.GOTO, result=label_end)

        # Define label for 'else' branch
        self.code_generator.emit(Operation.LABEL, result=label_else)

        # If 'else' branch exists, visit it
        if ctx.statement(1):
            self.visit(ctx.statement(1))

        # Define the end label if it exists
        if label_end:
            self.code_generator.emit(Operation.LABEL, result=label_end)

        return None

    def visitPrintStmt(self, ctx: CompiscriptParser.PrintStmtContext):
        # Evaluate the expression to be printed
        expr_temp = self.visit(ctx.expression())
        # Emit the PRINT instruction
        self.code_generator.emit(Operation.PRINT, arg1=expr_temp)
        return None

    # returnStmt: 'return' expression? ';';
    def visitReturnStmt(self, ctx: CompiscriptParser.ReturnStmtContext):
        if ctx.expression():
            ret_val = self.visit(ctx.expression())
            self.code_generator.emit(Operation.RETURN, arg1=ret_val)
        else:
            self.code_generator.emit(Operation.RETURN)
        return None

    def visitWhileStmt(self, ctx: CompiscriptParser.WhileStmtContext):
        # generate the while label for return to the start of the loop
        while_label = self.code_generator.new_label()
        # generate the break label for breaking out of the loop
        break_label = self.code_generator.new_label()
        self.code_generator.emit(Operation.LABEL, result=while_label)
        # get the expression type by visiting the expression
        condition = self.visit(ctx.expression())
        # generate the if_false instruction to break out of the loop
        self.code_generator.emit(
            Operation.IF_FALSE, arg1=condition, arg2="GOTO", result=break_label
        )
        # visit the block of code
        self.visit(ctx.statement())
        # emit the goto instruction to return to the start of the loop
        self.code_generator.emit(Operation.GOTO, result=while_label)
        # emit the label for the break
        self.code_generator.emit(Operation.LABEL, result=break_label)
        return None

    # breakStmt: 'break' ';'
    def visitBreakStmt(self, ctx: CompiscriptParser.BreakStmtContext):
        return self.visitChildren(ctx)

    # continueStmt: 'continue' ';'
    def visitContinueStmt(self, ctx: CompiscriptParser.ContinueStmtContext):
        return self.visitChildren(ctx)

    # block: '{' declaration* '}'
    def visitBlock(self, ctx: CompiscriptParser.BlockContext):
        return self.visitChildren(ctx)

    # assignment: (call '.')? IDENTIFIER ('+'|'-')? '=' assignment | logicOr | IDENTIFIER ('++' | '--')
    def visitAssignment(self, ctx: CompiscriptParser.AssignmentContext):
        if ctx.IDENTIFIER() is not None:
            # This is an assignment like 'x = ...'
            var_name = ctx.IDENTIFIER().getText()
            # Evaluate the right-hand side
            expr_result = self.visit(
                ctx.assignment() if ctx.assignment() else ctx.logicOr()
            )
            # Assign the result to the variable
            self.code_generator.emit(
                op=Operation.ASSIGN, arg1=expr_result, result=var_name
            )
            return var_name
        else:
            # Handle 'this' or 'super' assignments if necessary
            # For now, we treat other cases as expressions
            return self.visit(ctx.logicOr())

    # expression: assignment | funAnon
    def visitExpression(self, ctx: CompiscriptParser.ExpressionContext):
        # An expression can be an assignment or an anonymous function
        return self.visit(ctx.assignment() or ctx.funAnon())

    # logicOr: logicAnd ('or' logicAnd)*
    def visitLogicOr(self, ctx: CompiscriptParser.LogicOrContext):
        return self.visitChildren(ctx)

    # logicAnd: equality ('and' equality)*
    def visitLogicAnd(self, ctx: CompiscriptParser.LogicAndContext):
        return self.visitChildren(ctx)

    # equality: comparison (( '!=' | '==') comparison)*
    def visitEquality(self, ctx: CompiscriptParser.EqualityContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.comparison(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.comparison(1))

            temp = self.code_generator.new_temp()

            if operator == "==":
                op = Operation.EQ
            elif operator == "!=":
                op = Operation.NE
            else:
                raise Exception(f"Unknown equality operator: {operator}")

            self.code_generator.emit(op=op, arg1=left, arg2=right, result=temp)

            return temp
        else:
            return self.visit(ctx.comparison(0))

    # comparison: term (( '>' | '>=' | '<' | '<=') term)*
    def visitComparison(self, ctx: CompiscriptParser.ComparisonContext):
        # Start by visiting the first term
        left = self.visit(ctx.term(0))

        # Iterate over each comparison operator and the corresponding term
        for i in range(1, len(ctx.term())):
            operator = ctx.getChild(
                2 * i - 1
            ).getText()  # Operators are at odd positions
            right = self.visit(ctx.term(i))

            # Generate a new temporary variable to store the result
            temp = self.code_generator.new_temp()

            # Map the operator to the corresponding TAC operation
            if operator == ">":
                op = Operation.GT
            elif operator == ">=":
                op = Operation.GE
            elif operator == "<":
                op = Operation.LT
            elif operator == "<=":
                op = Operation.LE
            else:
                raise Exception(f"Unknown comparison operator: {operator}")

            # Emit the TAC instruction
            self.code_generator.emit(op=op, arg1=left, arg2=right, result=temp)

            # The result becomes the left operand for the next comparison if any
            left = temp

        return left

    # term: factor (( '-' | '+') factor)*
    def visitTerm(self, ctx: CompiscriptParser.TermContext):
        # Start by visiting the first factor
        left = self.visit(ctx.factor(0))

        # Iterate over each '+' or '-' operator and the corresponding factor
        for i in range(1, len(ctx.factor())):
            operator = ctx.getChild(
                2 * i - 1
            ).getText()  # Operators are at odd positions
            right = self.visit(ctx.factor(i))

            # Generate a new temporary variable to store the result
            temp = self.code_generator.new_temp()

            # Map the operator to the corresponding TAC operation
            if operator == "+":
                op = Operation.ADD
            elif operator == "-":
                op = Operation.SUB
            else:
                raise Exception(f"Unknown term operator: {operator}")

            # Emit the TAC instruction
            self.code_generator.emit(op=op, arg1=left, arg2=right, result=temp)

            # The result becomes the left operand for the next operation if any
            left = temp

        return left

    # factor: unary (( '/' | '*' | '%') unary)*
    def visitFactor(self, ctx: CompiscriptParser.FactorContext):
        # Start by visiting the first unary expression
        left = self.visit(ctx.unary(0))

        # Iterate over each '/', '*', or '%' operator and the corresponding unary expression
        for i in range(1, len(ctx.unary())):
            operator = ctx.getChild(
                2 * i - 1
            ).getText()  # Operators are at odd positions
            right = self.visit(ctx.unary(i))

            # Generate a new temporary variable to store the result
            temp = self.code_generator.new_temp()

            # Map the operator to the corresponding TAC operation
            if operator == "*":
                op = Operation.MUL
            elif operator == "/":
                op = Operation.DIV
            elif operator == "%":
                op = Operation.MOD
            else:
                raise Exception(f"Unknown factor operator: {operator}")

            # Emit the TAC instruction
            self.code_generator.emit(op=op, arg1=left, arg2=right, result=temp)

            # The result becomes the left operand for the next operation if any
            left = temp

        return left

    # unary: ( '!' | '-') unary | call
    def visitUnary(self, ctx: CompiscriptParser.UnaryContext):
        if ctx.getChildCount() == 2:
            # There's a unary operator and a unary expression
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.unary())

            # Generate a new temporary variable to store the result
            temp = self.code_generator.new_temp()

            # Map the operator to the corresponding TAC operation
            if operator == "!":
                op = Operation.NOT
            elif operator == "-":
                op = Operation.NEG
            else:
                raise Exception(f"Unknown unary operator: {operator}")

            # Emit the TAC instruction
            self.code_generator.emit(op=op, arg1=operand, result=temp)

            return temp
        else:
            # No unary operator; simply visit the call expression
            return self.visit(ctx.call())

    # instantiation: 'new' IDENTIFIER '(' arguments? ')'
    def visitInstantiation(self, ctx: CompiscriptParser.InstantiationContext):
        return self.visitChildren(ctx)

    # call: primary ( '(' arguments? ')' | '.' IDENTIFIER | '[' expression ']' )* | funAnon
    def visitCall(self, ctx: CompiscriptParser.CallContext):
        return self.visitChildren(ctx)

    # primary: 'true' | 'false' | 'nil' | 'this' | 'super' '.' IDENTIFIER | NUMBER | STRING | IDENTIFIER | '(' expression ')' | array | instantiation
    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            # Handle numeric literals
            return ctx.NUMBER().getText()
        elif ctx.STRING() is not None:
            # Handle string literals
            return ctx.STRING().getText()
        elif ctx.IDENTIFIER() is not None:
            if ctx.getChildCount() > 1 and ctx.getChild(1).getText() == "(":
                # Handle function calls
                return self.visit(ctx.call())
            else:
                return ctx.IDENTIFIER().getText()
        elif ctx.expression() is not None:
            # Handle expressions within parentheses
            return self.visit(ctx.expression())
        else:
            # Handle other literals like 'true', 'false', 'nil'
            temp = self.code_generator.new_temp()
            value = ctx.getText()
            self.code_generator.emit(op=Operation.ASSIGN, arg1=value, result=temp)
            return temp

    #  parameters: IDENTIFIER ( ',' IDENTIFIER)*
    def visitParameters(self, ctx: CompiscriptParser.ParametersContext):
        return self.visitChildren(ctx)

    # arguments: expression ( ',' expression)*
    def visitArguments(self, ctx: CompiscriptParser.ArgumentsContext):
        return self.visitChildren(ctx)


def generate_tac(code: str):
    try:
        input_stream = InputStream(code)
        lexer = CompiscriptLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CompiscriptParser(token_stream)
        tree = parser.program()

        visitor = CompiscriptCompiler()
        tac_instructions = visitor.visit(tree)

        # Convert the list of instructions to a string representation
        tac_output = "\n".join(str(instr) for instr in tac_instructions)

        return tac_output
    except Exception as e:
        return "An error occurred: " + str(e)

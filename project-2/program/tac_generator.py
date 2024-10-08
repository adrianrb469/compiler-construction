import sys

sys.path.append("..")
from typing import List

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
                print(f"Error during visit: {e} at {line}:{column}")
            else:
                print(f"Error during visit: {e}")
            return None

    def visitProgram(self, ctx: CompiscriptParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visit(declaration)
        # After visiting all declarations, return the generated code
        return self.code_generator.get_code()

    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        return self.visitChildren(ctx)

    def visitClassDecl(self, ctx: CompiscriptParser.ClassDeclContext):
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visit(ctx.function())

    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):
        var_name = ctx.IDENTIFIER().getText()
        if ctx.expression():
            # Evaluate the initializer expression
            expr_result = self.visit(ctx.expression())
            # If the expression is a literal value, assign it directly
            if isinstance(expr_result, str) and expr_result.isdigit():
                self.code_generator.emit(
                    op=Operation.ASSIGN, arg1=expr_result, result=var_name
                )
            else:
                # Assign the result to the variable
                self.code_generator.emit(
                    op=Operation.ASSIGN, arg1=expr_result, result=var_name
                )
        else:
            # No initializer; assign a default value (e.g., 0)
            self.code_generator.emit(op=Operation.ASSIGN, arg1="0", result=var_name)
        return var_name

    def visitFunction(self, ctx: CompiscriptParser.FunctionContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: CompiscriptParser.StatementContext):
        return self.visitChildren(ctx)

    def visitExprStmt(self, ctx: CompiscriptParser.ExprStmtContext):
        # Evaluate the expression statement
        self.visit(ctx.expression())
        return None

    def visitForStmt(self, ctx: CompiscriptParser.ForStmtContext):
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx: CompiscriptParser.IfStmtContext):
        # Evaluate the condition expression and get its temporary result
        condition = self.visit(ctx.expression())

        # Generate unique labels for else branch and end of if
        label_else = self.code_generator.new_label()
        label_end = self.code_generator.new_label()

        # Emit IF_FALSE condition GOTO label_else
        self.code_generator.emit(
            Operation.IF_FALSE, arg1=condition, arg2="GOTO", result=label_else
        )

        # Visit the 'then' statement
        self.visit(ctx.statement(0))

        # After 'then' block, jump to the end
        self.code_generator.emit(Operation.GOTO, result=label_end)

        # Define label for 'else' branch
        self.code_generator.emit(Operation.LABEL, result=label_else)

        # If 'else' branch exists, visit it
        if ctx.statement(1):
            self.visit(ctx.statement(1))

        # Define the end label
        self.code_generator.emit(Operation.LABEL, result=label_end)

        return None

    def visitPrintStmt(self, ctx: CompiscriptParser.PrintStmtContext):
        return self.visitChildren(ctx)

    def visitReturnStmt(self, ctx: CompiscriptParser.ReturnStmtContext):
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx: CompiscriptParser.WhileStmtContext):
        # generate the while label for return to the start of the loop
        while_label = self.code_generator.new_label()
        # generate the break label for breaking out of the loop
        break_label = self.code_generator.new_label()
        self.code_generator.emit(Operation.LABEL, result=while_label)
        # get the expression type by visiting the expression
        condition = self.visit(ctx.expression())
        # generate the if_false instruction to break out of the loop
        self.code_generator.emit(Operation.IF_FALSE, arg1=condition, arg2="GOTO", result=break_label)
        # visit the block of code
        self.visit(ctx.statement())
        # emit the goto instruction to return to the start of the loop
        self.code_generator.emit(Operation.GOTO, result=while_label)
        # emit the label for the break
        self.code_generator.emit(Operation.LABEL, result=break_label)
        return None

    def visitBreakStmt(self, ctx: CompiscriptParser.BreakStmtContext):
        return self.visitChildren(ctx)

    def visitContinueStmt(self, ctx: CompiscriptParser.ContinueStmtContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx: CompiscriptParser.BlockContext):
        return self.visitChildren(ctx)

    def visitFunAnon(self, ctx: CompiscriptParser.FunAnonContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: CompiscriptParser.AssignmentContext):
        if ctx.IDENTIFIER() is not None:
            # This is an assignment like 'x = ...'
            var_name = ctx.IDENTIFIER().getText()
            # Evaluate the right-hand side
            expr_temp = self.visit(
                ctx.assignment() if ctx.assignment() else ctx.logicOr()
            )
            # Assign the result to the variable
            self.code_generator.emit(
                op=Operation.ASSIGN, arg1=expr_temp, result=var_name
            )
            return var_name
        else:
            # Handle 'this' or 'super' assignments if necessary
            # For now, we treat other cases as expressions
            return self.visit(ctx.logicOr())

    def visitExpression(self, ctx: CompiscriptParser.ExpressionContext):
        # An expression can be an assignment or an anonymous function
        return self.visit(ctx.assignment() or ctx.funAnon())

    def visitLogicOr(self, ctx: CompiscriptParser.LogicOrContext):
        return self.visitChildren(ctx)

    def visitLogicAnd(self, ctx: CompiscriptParser.LogicAndContext):
        return self.visitChildren(ctx)

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

    def visitComparison(self, ctx: CompiscriptParser.ComparisonContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.term(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.term(1))

            # Generate a temporary variable for the condition result
            temp = self.code_generator.new_temp()

            # Map operators to TAC operations
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

            # Emit the comparison operation
            self.code_generator.emit(op=op, arg1=left, arg2=right, result=temp)

            return temp
        else:
            return self.visit(ctx.term(0))

    def visitTerm(self, ctx: CompiscriptParser.TermContext):
        if ctx.getChildCount() == 1:
            # Single factor; no operation needed
            return self.visit(ctx.factor(0))
        else:
            # Left operand
            left_temp = self.visit(ctx.factor(0))
            # Operator ('+' or '-')
            op = ctx.getChild(1).getText()
            # Right operand
            right_temp = self.visit(ctx.factor(1))
            # Generate a new temporary variable for the result
            result_temp = self.code_generator.new_temp()
            # Map the operator to the corresponding operation
            if op == "+":
                operation = Operation.ADD
            elif op == "-":
                operation = Operation.SUB
            else:
                raise Exception(f"Unknown operator {op}")
            # Emit the instruction
            self.code_generator.emit(
                op=operation, arg1=left_temp, arg2=right_temp, result=result_temp
            )
            return result_temp

    def visitFactor(self, ctx: CompiscriptParser.FactorContext):
        if ctx.getChildCount() == 1:
            # Single unary expression; no operation needed
            return self.visit(ctx.unary(0))
        else:
            # Left operand
            left_temp = self.visit(ctx.unary(0))
            # Operator ('*', '/', '%')
            op = ctx.getChild(1).getText()
            # Right operand
            right_temp = self.visit(ctx.unary(1))
            # Generate a new temporary variable for the result
            result_temp = self.code_generator.new_temp()
            # Map the operator to the corresponding operation
            if op == "*":
                operation = Operation.MUL
            elif op == "/":
                operation = Operation.DIV
            elif op == "%":
                operation = Operation.MOD  # Ensure MOD is added to the Operation enum
            else:
                raise Exception(f"Unknown operator {op}")
            # Emit the instruction
            self.code_generator.emit(
                op=operation, arg1=left_temp, arg2=right_temp, result=result_temp
            )
            return result_temp

    def visitUnary(self, ctx: CompiscriptParser.UnaryContext):
        return self.visitChildren(ctx)

    def visitArray(self, ctx: CompiscriptParser.ArrayContext):
        return self.visitChildren(ctx)

    def visitInstantiation(self, ctx: CompiscriptParser.InstantiationContext):
        return self.visitChildren(ctx)

    def visitCall(self, ctx: CompiscriptParser.CallContext):
        # Corrected to avoid infinite recursion
        return self.visitChildren(ctx)

    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            # Handle numeric literals
            return ctx.NUMBER().getText()
        elif ctx.STRING() is not None:
            # Handle string literals
            return ctx.STRING().getText()
        elif ctx.IDENTIFIER() is not None:
            # Return the variable name directly
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

    def visitParameters(self, ctx: CompiscriptParser.ParametersContext):
        return self.visitChildren(ctx)

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

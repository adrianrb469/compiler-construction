import sys

sys.path.append("..")
from typing import List
from antlr4 import *
from .CompiscriptLexer import CompiscriptLexer
from .CompiscriptParser import CompiscriptParser
from .CompiscriptVisitor import CompiscriptVisitor
from .SymbolTable import ClassSymbol, DataType, FunctionSymbol, SymbolTable, SymbolType
from utils.utils import getDeclType, types_comparable, arithmetic_op


class CompiscriptCompiler(CompiscriptVisitor):
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.current_class = None
        self.current_function = None
        self.errors: List[str] = []
        self.loop_depth = 0

    def report_error(self, message: str, ctx):
        line = ctx.start.line
        column = ctx.start.column
        self.errors.append(f"Error at line {line}, column {column}: {message}")

    def visitProgram(self, ctx: CompiscriptParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visit(declaration)

        for error in self.errors:
            print(error)
        return None

    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        if ctx.classDecl() is not None:
            return self.visitClassDecl(ctx.classDecl())
        elif ctx.funDecl() is not None:
            return self.visitFunDecl(ctx.funDecl())
        elif ctx.varDecl() is not None:
            return self.visitVarDecl(ctx.varDecl())
        else:  # return the statement at self as the last option
            return self.visitStatement(ctx.statement())

    def visitClassDecl(self, ctx: CompiscriptParser.ClassDeclContext):
        # Get the class name
        class_name = ctx.IDENTIFIER(0).getText()
        if self.symbol_table.lookup(class_name, current_scope_only=True):
            exp_type = str(
                self.symbol_table.lookup(class_name, current_scope_only=True).data_type
            ).replace("DataType.", "")
            self.report_error(
                f"Variable '{class_name}' already defined as {getDeclType(exp_type)}",
                ctx,
            )
            return None

        # Manage inheritance
        extensions = ctx.IDENTIFIER()
        parent_classes = []
        if len(extensions) > 1:
            parent_class_name = extensions[1].getText()
            parent_class = self.symbol_table.lookup(parent_class_name)
            if not parent_class:
                self.report_error(f"Class '{parent_class_name}' not defined", ctx)
                return None
            parent_classes.append(parent_class)

        # Create the new class symbol
        new_class = self.symbol_table.declare_symbol(
            class_name,
            SymbolType.CLASS,
            DataType.OBJECT,
            ctx.start.line,
            ctx.start.column,
        )
        assert isinstance(new_class, ClassSymbol)

        # Enter the class scope
        self.symbol_table.enter_scope(class_name)
        self.current_class = new_class

        # Inherit methods from parent class
        for parent_class in parent_classes:
            print(f"parent class methods: {parent_class.methods}")
            for method_name, method in parent_class.methods.items():
                print(
                    f"Inheriting method in {class_name} from {parent_class.name}:",
                    method_name,
                )
                if method_name not in new_class.methods:
                    # add the inherited method to the new class methods dictionary
                    new_class.methods[method_name] = method
                    # Also add the inherited method to the current scope
                    self.symbol_table.declare_symbol(
                        method_name,
                        SymbolType.FUNCTION,
                        method.data_type,
                        ctx.start.line,
                        ctx.start.column,
                    )

        methods = ctx.methods()
        init_count = 0

        for method in methods.getChildren():
            if isinstance(method, CompiscriptParser.InitContext):
                # find if there are this.varname in the init
                # if there are, add them to the class symbol table

                print(f"Found initializer in class {class_name}")
                self.symbol_table.enter_scope("init")
                self.visit(method)
                self.symbol_table.exit_scope()
                init_count += 1
                if init_count > 1:
                    self.report_error(
                        f'Multiple initializers found in class "{class_name}"', ctx
                    )
                    return None
            self.visit(method)

        print(f"this statements: {vars(new_class.attributes)}")

        # Exit the class scope
        self.symbol_table.exit_scope()
        self.current_class = None

        return None

    def visitInit(self, ctx: CompiscriptParser.InitContext):
        # verify that the initializer is in a class context
        if not self.current_class:
            self.report_error("Initializer outside of class context", ctx)
            return None

        # Get the initializer name as this.attribute = value
        parameters = ctx.parameters()

        # save parameters as a normal function
        for param in parameters.IDENTIFIER():
            param_name = param.getText()
            self.symbol_table.declare_symbol(
                param_name,
                SymbolType.VARIABLE,
                DataType.ANY,
                param.getPayload().line,
                param.getPayload().column,
            )

        self.visit(ctx.block())

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visit(ctx.function())

    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):

        var_name = ctx.IDENTIFIER().getText()

        if self.symbol_table.lookup(var_name, current_scope_only=True):
            self.report_error(f"Variable '{var_name}' already defined", ctx)
            return None

        if ctx.expression():
            print(
                f"Declaring variable {var_name} with type {self.visit(ctx.expression())}"
            )

            expr_type = self.visit(ctx.expression())
            self.symbol_table.declare_symbol(
                var_name,
                SymbolType.VARIABLE,
                expr_type,
                ctx.start.line,
                ctx.start.column,
            )
        else:
            self.symbol_table.declare_symbol(
                var_name,
                SymbolType.VARIABLE,
                DataType.ANY,
                ctx.start.line,
                ctx.start.column,
            )
        return None

    def visitFunction(self, ctx: CompiscriptParser.FunctionContext):
        fun_name = ctx.IDENTIFIER().getText()

        if self.symbol_table.lookup(fun_name, current_scope_only=True):
            self.report_error(f"Function '{fun_name}' already defined", ctx)
            return None

        # TODO: Actually infer the return type from the function body
        fun_symbol = self.symbol_table.declare_symbol(
            fun_name,
            SymbolType.FUNCTION,
            DataType.ANY,
            ctx.start.line,
            ctx.start.column,
        )
        assert isinstance(fun_symbol, FunctionSymbol)

        self.current_function = fun_symbol
        self.symbol_table.enter_scope(fun_name)

        if ctx.parameters():
            self.visit(ctx.parameters())

        self.visit(ctx.block())

        self.symbol_table.exit_scope()
        self.current_function = None

        if self.current_class:
            self.current_class.methods[fun_name] = fun_symbol

        return None

    def visitStatement(self, ctx: CompiscriptParser.StatementContext):
        return self.visitChildren(ctx)

    def visitExprStmt(self, ctx: CompiscriptParser.ExprStmtContext):
        return self.visitChildren(ctx)

    def visitForStmt(self, ctx: CompiscriptParser.ForStmtContext):
        self.symbol_table.enter_scope("for")
        self.loop_depth += 1

        # Initializer
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            self.visit(ctx.exprStmt())
        # If neither, it's an empty initializer (just a semicolon)

        # Condition
        if ctx.expression(0):
            condition_type = self.visit(ctx.expression(0))
            if condition_type != DataType.BOOLEAN:
                self.report_error(
                    f"For loop condition must be a boolean, got {condition_type}",
                    ctx.expression(0),
                )

        # Increment
        if ctx.expression(1):
            self.visit(ctx.expression(1))

        # Body
        self.visit(ctx.statement())
        self.symbol_table.exit_scope()

        self.loop_depth -= 1
        return None

    def visitIfStmt(self, ctx: CompiscriptParser.IfStmtContext):
        condition_type = self.visit(ctx.expression())
        if condition_type != DataType.BOOLEAN:
            self.report_error(
                f"Condition in if statement must evaluate to Boolean, got {condition_type.name}",
                ctx,
            )
            return None

        # 'If' branch
        self.symbol_table.enter_scope("if")
        result = self.visit(ctx.statement(0))
        self.symbol_table.exit_scope()

        # 'Else' branch (if it exists)
        if len(ctx.statement()) > 1:
            self.symbol_table.enter_scope("else")
            else_result = self.visit(ctx.statement(1))
            self.symbol_table.exit_scope()
        else:
            else_result = None

        return result if condition_type else else_result

    def visitPrintStmt(self, ctx: CompiscriptParser.PrintStmtContext):
        return self.visitChildren(ctx)

    def visitReturnStmt(self, ctx: CompiscriptParser.ReturnStmtContext):
        if not self.current_function:
            self.report_error("Return statement outside of function", ctx)
            return None

        if ctx.expression():
            return_type = self.visit(ctx.expression())
            if self.current_function.data_type == DataType.VOID:
                self.report_error("Cannot return a value from a void function", ctx)
            elif (
                self.current_function.data_type is not DataType.ANY
                and return_type != self.current_function.data_type
            ):
                self.report_error(
                    f"Return type mismatch. Expected {self.current_function.data_type}, got {return_type}",
                    ctx,
                )
        elif self.current_function.data_type != DataType.VOID:
            self.report_error(
                f"Function must return a value of type {self.current_function.data_type}",
                ctx,
            )

        return None  # Return statements don't have a type themselves

    def visitWhileStmt(self, ctx: CompiscriptParser.WhileStmtContext):
        self.loop_depth += 1
        condition_type = self.visit(ctx.expression())
        if condition_type != DataType.BOOLEAN:
            self.report_error(
                f"While condition must be a boolean, got {condition_type}",
                ctx.expression(),
            )

        self.symbol_table.enter_scope("while")
        self.visit(ctx.statement())
        self.symbol_table.exit_scope()
        self.loop_depth -= 1
        return None  # While statements don't have a type

    def visitBreakStmt(self, ctx: CompiscriptParser.BreakStmtContext):
        if self.loop_depth == 0:
            print("Break statement outside of loop")
            self.report_error("'break' statement outside of loop", ctx)
        return None

    def visitContinueStmt(self, ctx: CompiscriptParser.ContinueStmtContext):
        if self.loop_depth == 0:
            self.report_error("'continue' statement outside of loop", ctx)
        return None

    def visitBlock(self, ctx: CompiscriptParser.BlockContext):
        # self.symbol_table.enter_scope("block")  # does it need a name?
        for declaration in ctx.declaration():
            self.visit(declaration)
        # self.symbol_table.exit_scope()
        return None

    def visitFunAnon(self, ctx: CompiscriptParser.FunAnonContext):
        return self.visitChildren(ctx)

    def visitExpression(self, ctx: CompiscriptParser.ExpressionContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.funAnon():
            return self.visit(ctx.funAnon())
        return DataType.ANY

    def visitAssignment(self, ctx: CompiscriptParser.AssignmentContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            symbol = self.symbol_table.lookup(var_name)
            if not symbol:
                self.report_error(f"Variable '{var_name}' not defined", ctx)
                return DataType.ANY

            if ctx.assignment():
                expr_type = self.visit(ctx.assignment())
            else:
                expr_type = self.visit(ctx.logicOr())

            print(f"Assignment to {var_name}: {expr_type}")

            if symbol.data_type != DataType.ANY and symbol.data_type != expr_type:
                self.report_error(
                    f"Type mismatch in assignment to '{var_name}', expected {symbol.data_type} but got {expr_type}",
                    ctx,
                )
            return expr_type
        else:
            return self.visit(ctx.logicOr())

    def visitLogicOr(self, ctx: CompiscriptParser.LogicOrContext):
        left = self.visit(ctx.logicAnd(0))

        if len(ctx.logicAnd()) == 1:
            return left

        for i in range(1, len(ctx.logicAnd())):
            right = self.visit(ctx.logicAnd(i))
            if left != DataType.BOOLEAN or right != DataType.BOOLEAN:
                self.report_error(
                    f"Operands of OR must be boolean, got {left.name} and {right.name}",
                    ctx,
                )
                return DataType.ANY

        return DataType.BOOLEAN

    def visitLogicAnd(self, ctx: CompiscriptParser.LogicAndContext):
        left = self.visit(ctx.equality(0))

        if len(ctx.equality()) == 1:
            return left

        for i in range(1, len(ctx.equality())):
            right = self.visit(ctx.equality(i))
            if right != DataType.BOOLEAN:
                self.report_error(
                    f"Right operand of AND must be boolean, got {right.name}", ctx
                )
                return DataType.ANY

        return DataType.BOOLEAN

    def visitEquality(self, ctx: CompiscriptParser.EqualityContext):
        left = self.visit(ctx.comparison(0))

        if len(ctx.comparison()) == 1:
            return left

        for i in range(1, len(ctx.comparison())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.comparison(i))
            if not types_comparable(left, right):
                self.report_error(
                    f"Type mismatch in comparison, cannot compare {left} with {right} using operator '{op}'",
                    ctx,
                )
                return DataType.ANY

        return DataType.BOOLEAN

    def visitComparison(self, ctx: CompiscriptParser.ComparisonContext):
        left = self.visit(ctx.term(0))

        if len(ctx.term()) == 1:
            return left

        for i in range(1, len(ctx.term())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.term(i))

            if not types_comparable(left, right):
                self.report_error(
                    f"Cannot compare {left.name} with {right.name} using {op}", ctx
                )
                return DataType.ANY

        return DataType.BOOLEAN

    def visitTerm(self, ctx: CompiscriptParser.TermContext):
        left = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.factor(i))

            result = arithmetic_op(left, op, right)

            if result is None:
                self.report_error(
                    f"Cannot perform operation {op} on {left.name} and {right.name}",
                    ctx,
                )
                return DataType.ANY

            left = result

        return left

    def visitFactor(self, ctx: CompiscriptParser.FactorContext):
        left = self.visitUnary(ctx.unary(0))

        if len(ctx.unary()) == 1:
            return left

        for i in range(1, len(ctx.unary())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.unary(i))

            result = arithmetic_op(left, op, right)

            if result is None:
                self.report_error(
                    f"Cannot perform operation {op} on {left.name} and {right.name}",
                    ctx,
                )
                return DataType.ANY

            left = result
        return left

    def visitUnary(self, ctx: CompiscriptParser.UnaryContext):
        if ctx.getChildCount() == 1:
            primary = self.visit(ctx.getChild(0))
            return primary

        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.getChild(1))  # think of -1, or !true

        if ctx.call() is not None:
            return self.visit(ctx.call())

        elif op == "-":
            if operand not in [DataType.INT, DataType.FLOAT]:
                self.report_error(
                    f"Invalid type for unary negation. Expected numeric type, got {operand.name}",
                    ctx,
                )
                return DataType.ANY
            return operand  # The type remains the same (INT or FLOAT)
        elif op == "!":
            if operand != DataType.BOOLEAN:
                self.report_error(
                    f"Invalid type for logical NOT. Expected Boolean, got {operand.name}",
                    ctx,
                )
                return DataType.ANY
            return DataType.BOOLEAN

        # If we reach here, it's an error (unexpected unary operator)
        self.report_error(f"Unexpected unary operator: {op}", ctx)
        return DataType.ANY

    def visitArray(self, ctx: CompiscriptParser.ArrayContext):
        return self.visitChildren(ctx)

    def visitInstantiation(self, ctx: CompiscriptParser.InstantiationContext):
        print("Instantiation of class" + ctx.IDENTIFIER().getText())
        # if the class is not defined, report an error
        class_name = ctx.IDENTIFIER().getText()
        if not self.symbol_table.lookup(class_name):
            self.report_error(f"Class '{class_name}' not defined", ctx)
            return DataType.ANY

        return self.visitChildren(ctx)

    def visitCall(self, ctx: CompiscriptParser.CallContext):
        return self.visitChildren(ctx)

    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):

        match ctx:
            case _ if ctx.NUMBER():
                return DataType.FLOAT if "." in ctx.NUMBER().getText() else DataType.INT

            case _ if ctx.STRING():
                return DataType.STRING

            case _ if ctx.IDENTIFIER():
                var_name = ctx.IDENTIFIER().getText()
                symbol = self.symbol_table.lookup(var_name)
                if not symbol:
                    self.report_error(f"Variable '{var_name}' not defined", ctx)
                    return DataType.ANY

                print("Variable found:", var_name, symbol.data_type, ctx.start.line)
                return symbol.data_type

            case _ if ctx.getChild(0).getText() in ["true", "false"]:
                return DataType.BOOLEAN

            case _ if ctx.getChild(0).getText() == "nil":
                return DataType.NULL

            case _ if ctx.getChild(0).getText() == "this":
                if not self.current_class:
                    self.report_error("'this' used outside of class context", ctx)
                return DataType.OBJECT

            case _ if ctx.expression():
                return self.visit(ctx.expression())

            case _ if ctx.getChild(0).getText() == "super":
                if not self.current_class or not self.current_class.superclass:
                    self.report_error("Invalid use of 'super'", ctx)
                return DataType.OBJECT

            case _ if ctx.array():
                return DataType.ARRAY

            case _ if ctx.instantiation():
                return DataType.OBJECT

            case _:
                return DataType.ANY

    def visitParameters(self, ctx: CompiscriptParser.ParametersContext):
        for param in ctx.IDENTIFIER():
            param_name = param.getText()
            param_symbol = self.symbol_table.declare_symbol(
                param_name,
                SymbolType.VARIABLE,
                DataType.ANY,
                param.getPayload().line,
                param.getPayload().column,
            )
            if self.current_function:
                self.current_function.parameters.append(param_symbol)
        return None

    def visitArguments(self, ctx: CompiscriptParser.ArgumentsContext):
        return self.visitChildren(ctx)

    def getErrors(self):
        return self.errors

    def getSymbolTable(self):
        return self.symbol_table


def main(argv):
    if len(argv) != 2:
        print("Usage: python3 Driver.py <input file>")
        sys.exit(1)

    input_file = argv[1]

    try:
        input_stream = FileStream(input_file)
        lexer = CompiscriptLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CompiscriptParser(token_stream)
        tree = parser.program()

        compiler = CompiscriptCompiler()
        compiler.visit(tree)

    except IOError as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)


def compiler(code):
    try:
        input_stream = InputStream(code)
        lexer = CompiscriptLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CompiscriptParser(token_stream)
        tree = parser.program()
        tree_str = tree.toStringTree(recog=parser)

        visitor = CompiscriptCompiler()
        visitor.visit(tree)
        errors = visitor.getErrors()

        table = visitor.getSymbolTable().to_dict()

        return tree_str, errors, table
    except Exception as e:
        print("Error compiling code", e)
        return None, [str(e)]

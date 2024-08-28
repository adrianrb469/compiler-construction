import sys
from typing import List
from antlr4 import *
from .CompiscriptLexer import CompiscriptLexer
from .CompiscriptParser import CompiscriptParser
from .CompiscriptVisitor import CompiscriptVisitor
from .SymbolTable import DataType, FunctionSymbol, SymbolTable, SymbolType


class CompiscriptCompiler(CompiscriptVisitor):
    def __init__(self) -> None:
        self.symbol_table = SymbolTable("global")
        self.current_class = None
        self.errors: List[str] = []

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
        return self.visitChildren(ctx)

    def visitClassDecl(self, ctx: CompiscriptParser.ClassDeclContext):
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):

        var_name = ctx.IDENTIFIER().getText()

        if self.symbol_table.lookup(var_name, current_scope=True):
            self.report_error(f"Variable '{var_name}' already defined", ctx)
            return None

        if ctx.expression():
            # var a = 4+5
            #  var b = random()
            expr_type = self.visit(ctx.expression())
            self.symbol_table.declare_symbol(
                var_name,
                SymbolType.VARIABLE,
                expr_type,
                ctx.start.line,
                ctx.start.column,
            )
        else:
            # var a;
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

        if self.symbol_table.lookup(fun_name, current_scope=True):
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
        self.symbol_table.enter_scope()

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
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx: CompiscriptParser.IfStmtContext):
        return self.visitChildren(ctx)

    def visitPrintStmt(self, ctx: CompiscriptParser.PrintStmtContext):
        return self.visitChildren(ctx)

    def visitReturnStmt(self, ctx: CompiscriptParser.ReturnStmtContext):
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx: CompiscriptParser.WhileStmtContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx: CompiscriptParser.BlockContext):
        self.symbol_table.enter_scope()
        for declaration in ctx.declaration():
            self.visit(declaration)
        self.symbol_table.exit_scope()
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

            expr_type = self.visit(ctx.assignment())
            if symbol.data_type != DataType.ANY and symbol.data_type != expr_type:
                self.report_error(
                    f"Type mismatch in assignment to '{var_name}', expected {symbol.data_type} but got {expr_type}",
                    ctx,
                )

            return symbol.data_type
        else:
            return self.visit(ctx.logicOr())

    def visitLogicOr(self, ctx: CompiscriptParser.LogicOrContext):
        return self.visitChildren(ctx)

    def visitLogicAnd(self, ctx: CompiscriptParser.LogicAndContext):
        return self.visitChildren(ctx)

    def visitEquality(self, ctx: CompiscriptParser.EqualityContext):
        return self.visitChildren(ctx)

    def visitComparison(self, ctx: CompiscriptParser.ComparisonContext):
        return self.visitChildren(ctx)

    def visitTerm(self, ctx: CompiscriptParser.TermContext):
        return self.visitChildren(ctx)

    def visitFactor(self, ctx: CompiscriptParser.FactorContext):
        return self.visitChildren(ctx)

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

    def visitUnary(self, ctx: CompiscriptParser.UnaryContext):
        return self.visitChildren(ctx)

    def visitCall(self, ctx: CompiscriptParser.CallContext):
        return self.visitChildren(ctx)

    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):
        if ctx.NUMBER():
            return DataType.FLOAT if "." in ctx.NUMBER().getText() else DataType.INT
        elif ctx.STRING():
            return DataType.STRING
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            symbol = self.symbol_table.lookup(var_name)
            if not symbol:
                self.report_error(f"Variable '{var_name}' not defined", ctx)
                return DataType.ANY
            return symbol.data_type
        elif (
            ctx.getChild(0).getText() == "true" or ctx.getChild(0).getText() == "false"
        ):
            return DataType.BOOLEAN
        elif ctx.getChild(0).getText() == "nil":
            return DataType.ANY
        elif ctx.getChild(0).getText() == "this":
            if not self.current_class:
                self.report_error("'this' used outside of class context", ctx)
            return DataType.OBJECT
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.getChild(0).getText() == "super":
            if not self.current_class or not self.current_class.superclass:
                self.report_error("Invalid use of 'super'", ctx)
            return DataType.OBJECT
        elif ctx.array():
            return DataType.ARRAY
        elif ctx.instantiation():
            return DataType.OBJECT
        return DataType.ANY

    def visitParameters(self, ctx: CompiscriptParser.ParametersContext):
        for param in ctx.IDENTIFIER():
            param_name = param.getText()
            param_symbol = self.symbol_table.declare_symbol(
                param_name,
                SymbolType.PARAMETER,
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

        return tree_str, errors
    except Exception as e:
        print("Error compiling code", e)
        return None, [str(e)]

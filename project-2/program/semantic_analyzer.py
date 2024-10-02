import sys
sys.path.append("..")
from typing import List
from antlr4 import *
from .CompiscriptLexer import CompiscriptLexer
from .CompiscriptParser import CompiscriptParser
from .CompiscriptVisitor import CompiscriptVisitor
from .SymbolTable import (
    ClassSymbol,
    DataType,
    FunctionSymbol,
    SymbolTable,
    SymbolType,
    Symbol,
    UnionType,
)
from utils.utils import getDeclType, types_comparable, arithmetic_op

class CompiscriptCompiler(CompiscriptVisitor):
    def __init__(self) -> None:
        self.temp_variables = []

    def visit(self, tree):
        if tree is None:
            print("Error: Attempting to visit None")
            return DataType.ANY
        try:
            return super().visit(tree)
        except Exception as e:
            print(f"Error during visit: {e}")
            return DataType.ANY

    def visitProgram(self, ctx: CompiscriptParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visit(declaration)

        return None

    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        return self.visitChildren(ctx)

    def visitClassDecl(self, ctx: CompiscriptParser.ClassDeclContext):
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visit(ctx.function())

    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):
        return self.visitChildren(ctx)

    def visitFunction(self, ctx: CompiscriptParser.FunctionContext):
        return self.visitChildren(ctx)

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

    def visitBreakStmt(self, ctx: CompiscriptParser.BreakStmtContext):
        return self.visitChildren(ctx)

    def visitContinueStmt(self, ctx: CompiscriptParser.ContinueStmtContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx: CompiscriptParser.BlockContext):
        return self.visitChildren(ctx)

    def visitFunAnon(self, ctx: CompiscriptParser.FunAnonContext):
        return self.visitChildren(ctx)

    def visitExpression(self, ctx: CompiscriptParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: CompiscriptParser.AssignmentContext):
      return self.visitChildren(ctx)

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

    def visitUnary(self, ctx: CompiscriptParser.UnaryContext):
        return self.visitChildren(ctx)

    def visitArray(self, ctx: CompiscriptParser.ArrayContext):
        return self.visitChildren(ctx)

    def visitInstantiation(self, ctx: CompiscriptParser.InstantiationContext):
        return self.visitChildren(ctx)

    def visitCall(self, ctx: CompiscriptParser.CallContext):
        return self.visit(ctx)

    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):
        return self.visitChildren(ctx)

    def visitParameters(self, ctx: CompiscriptParser.ParametersContext):
        return self.visitChildren(ctx)

    def visitArguments(self, ctx: CompiscriptParser.ArgumentsContext):
        return self.visitChildren(ctx)

def compile_code(code):
    try:
        input_stream = InputStream(code)
        lexer = CompiscriptLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CompiscriptParser(token_stream)
        tree = parser.program()
        tree_str = tree.toStringTree(recog=parser)

        visitor = CompiscriptCompiler()
        visitor.visit(tree)

        return code
    except Exception as e:
        return "an error occurred: " + str(e)

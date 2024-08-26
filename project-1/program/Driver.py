import sys
from antlr4 import *
from CompiscriptLexer import CompiscriptLexer
from CompiscriptParser import CompiscriptParser
from CompiscriptVisitor import CompiscriptVisitor


class CompiscriptCompiler(CompiscriptVisitor):
    def visitProgram(self, ctx: CompiscriptParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        return self.visitChildren(ctx)

    def visitClassDecl(self, ctx: CompiscriptParser.ClassDeclContext):
        return self.visitChildren(ctx)

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):
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

    def visitArray(self, ctx: CompiscriptParser.ArrayContext):
        return self.visitChildren(ctx)

    def visitInstantiation(self, ctx: CompiscriptParser.InstantiationContext):
        return self.visitChildren(ctx)

    def visitUnary(self, ctx: CompiscriptParser.UnaryContext):
        return self.visitChildren(ctx)

    def visitCall(self, ctx: CompiscriptParser.CallContext):
        return self.visitChildren(ctx)

    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):
        return self.visitChildren(ctx)

    def visitFunction(self, ctx: CompiscriptParser.FunctionContext):
        return self.visitChildren(ctx)

    def visitParameters(self, ctx: CompiscriptParser.ParametersContext):
        return self.visitChildren(ctx)

    def visitArguments(self, ctx: CompiscriptParser.ArgumentsContext):
        return self.visitChildren(ctx)


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

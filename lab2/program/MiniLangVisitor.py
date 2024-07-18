# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#prog.
    def visitProg(self, ctx:MiniLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#printExpr.
    def visitPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assign.
    def visitAssign(self, ctx:MiniLangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ifStat.
    def visitIfStat(self, ctx:MiniLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#whileStat.
    def visitWhileStat(self, ctx:MiniLangParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#blank.
    def visitBlank(self, ctx:MiniLangParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#unrecognizedToken.
    def visitUnrecognizedToken(self, ctx:MiniLangParser.UnrecognizedTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ifBlock.
    def visitIfBlock(self, ctx:MiniLangParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#whileBlock.
    def visitWhileBlock(self, ctx:MiniLangParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assignment.
    def visitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#parens.
    def visitParens(self, ctx:MiniLangParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#compare.
    def visitCompare(self, ctx:MiniLangParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MulDiv.
    def visitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AddSub.
    def visitAddSub(self, ctx:MiniLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#id.
    def visitId(self, ctx:MiniLangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#constantExpr.
    def visitConstantExpr(self, ctx:MiniLangParser.ConstantExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#compareOp.
    def visitCompareOp(self, ctx:MiniLangParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#constant.
    def visitConstant(self, ctx:MiniLangParser.ConstantContext):
        return self.visitChildren(ctx)



del MiniLangParser
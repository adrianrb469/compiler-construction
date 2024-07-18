# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#prog.
    def enterProg(self, ctx:MiniLangParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniLangParser#prog.
    def exitProg(self, ctx:MiniLangParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printExpr.
    def enterPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#printExpr.
    def exitPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assign.
    def enterAssign(self, ctx:MiniLangParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assign.
    def exitAssign(self, ctx:MiniLangParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ifStat.
    def enterIfStat(self, ctx:MiniLangParser.IfStatContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifStat.
    def exitIfStat(self, ctx:MiniLangParser.IfStatContext):
        pass


    # Enter a parse tree produced by MiniLangParser#whileStat.
    def enterWhileStat(self, ctx:MiniLangParser.WhileStatContext):
        pass

    # Exit a parse tree produced by MiniLangParser#whileStat.
    def exitWhileStat(self, ctx:MiniLangParser.WhileStatContext):
        pass


    # Enter a parse tree produced by MiniLangParser#blank.
    def enterBlank(self, ctx:MiniLangParser.BlankContext):
        pass

    # Exit a parse tree produced by MiniLangParser#blank.
    def exitBlank(self, ctx:MiniLangParser.BlankContext):
        pass


    # Enter a parse tree produced by MiniLangParser#unrecognizedToken.
    def enterUnrecognizedToken(self, ctx:MiniLangParser.UnrecognizedTokenContext):
        pass

    # Exit a parse tree produced by MiniLangParser#unrecognizedToken.
    def exitUnrecognizedToken(self, ctx:MiniLangParser.UnrecognizedTokenContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ifBlock.
    def enterIfBlock(self, ctx:MiniLangParser.IfBlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifBlock.
    def exitIfBlock(self, ctx:MiniLangParser.IfBlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#whileBlock.
    def enterWhileBlock(self, ctx:MiniLangParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#whileBlock.
    def exitWhileBlock(self, ctx:MiniLangParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#block.
    def enterBlock(self, ctx:MiniLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block.
    def exitBlock(self, ctx:MiniLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assignment.
    def enterAssignment(self, ctx:MiniLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assignment.
    def exitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniLangParser#parens.
    def enterParens(self, ctx:MiniLangParser.ParensContext):
        pass

    # Exit a parse tree produced by MiniLangParser#parens.
    def exitParens(self, ctx:MiniLangParser.ParensContext):
        pass


    # Enter a parse tree produced by MiniLangParser#compare.
    def enterCompare(self, ctx:MiniLangParser.CompareContext):
        pass

    # Exit a parse tree produced by MiniLangParser#compare.
    def exitCompare(self, ctx:MiniLangParser.CompareContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDiv.
    def enterMulDiv(self, ctx:MiniLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDiv.
    def exitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSub.
    def enterAddSub(self, ctx:MiniLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSub.
    def exitAddSub(self, ctx:MiniLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by MiniLangParser#id.
    def enterId(self, ctx:MiniLangParser.IdContext):
        pass

    # Exit a parse tree produced by MiniLangParser#id.
    def exitId(self, ctx:MiniLangParser.IdContext):
        pass


    # Enter a parse tree produced by MiniLangParser#constantExpr.
    def enterConstantExpr(self, ctx:MiniLangParser.ConstantExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#constantExpr.
    def exitConstantExpr(self, ctx:MiniLangParser.ConstantExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#compareOp.
    def enterCompareOp(self, ctx:MiniLangParser.CompareOpContext):
        pass

    # Exit a parse tree produced by MiniLangParser#compareOp.
    def exitCompareOp(self, ctx:MiniLangParser.CompareOpContext):
        pass


    # Enter a parse tree produced by MiniLangParser#constant.
    def enterConstant(self, ctx:MiniLangParser.ConstantContext):
        pass

    # Exit a parse tree produced by MiniLangParser#constant.
    def exitConstant(self, ctx:MiniLangParser.ConstantContext):
        pass



del MiniLangParser
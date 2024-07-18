# Generated from MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,1,2,
        3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,53,8,4,10,4,12,4,56,9,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,71,8,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,83,8,6,10,6,12,6,86,
        9,6,1,7,1,7,1,8,1,8,1,8,0,1,12,9,0,2,4,6,8,10,12,14,16,0,4,1,0,18,
        19,1,0,20,21,1,0,12,17,1,0,23,27,95,0,19,1,0,0,0,2,36,1,0,0,0,4,
        38,1,0,0,0,6,45,1,0,0,0,8,50,1,0,0,0,10,59,1,0,0,0,12,70,1,0,0,0,
        14,87,1,0,0,0,16,89,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,
        0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,24,5,1,0,0,24,
        25,5,2,0,0,25,26,3,12,6,0,26,27,5,3,0,0,27,28,5,4,0,0,28,37,1,0,
        0,0,29,30,3,10,5,0,30,31,5,4,0,0,31,37,1,0,0,0,32,37,3,4,2,0,33,
        37,3,6,3,0,34,37,5,28,0,0,35,37,5,31,0,0,36,23,1,0,0,0,36,29,1,0,
        0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,3,
        1,0,0,0,38,39,5,5,0,0,39,40,3,12,6,0,40,43,3,8,4,0,41,42,5,6,0,0,
        42,44,3,8,4,0,43,41,1,0,0,0,43,44,1,0,0,0,44,5,1,0,0,0,45,46,5,7,
        0,0,46,47,3,12,6,0,47,48,5,8,0,0,48,49,3,8,4,0,49,7,1,0,0,0,50,54,
        5,9,0,0,51,53,3,2,1,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,
        54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,58,5,10,0,0,58,9,1,
        0,0,0,59,60,5,22,0,0,60,61,5,11,0,0,61,62,3,12,6,0,62,11,1,0,0,0,
        63,64,6,6,-1,0,64,71,3,16,8,0,65,71,5,22,0,0,66,67,5,2,0,0,67,68,
        3,12,6,0,68,69,5,3,0,0,69,71,1,0,0,0,70,63,1,0,0,0,70,65,1,0,0,0,
        70,66,1,0,0,0,71,84,1,0,0,0,72,73,10,5,0,0,73,74,7,0,0,0,74,83,3,
        12,6,6,75,76,10,4,0,0,76,77,7,1,0,0,77,83,3,12,6,5,78,79,10,1,0,
        0,79,80,3,14,7,0,80,81,3,12,6,2,81,83,1,0,0,0,82,72,1,0,0,0,82,75,
        1,0,0,0,82,78,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,
        85,13,1,0,0,0,86,84,1,0,0,0,87,88,7,2,0,0,88,15,1,0,0,0,89,90,7,
        3,0,0,90,17,1,0,0,0,7,21,36,43,54,70,82,84
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "';'", "'if'", 
                     "'else'", "'while'", "'do'", "'{'", "'}'", "'='", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'*'", "'/'", 
                     "'+'", "'-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MUL", "DIV", "ADD", "SUB", 
                      "ID", "INT", "STRING", "BOOLEAN", "FLOAT", "NULL", 
                      "NEWLINE", "COMMENT", "WS", "INVALID_CHAR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_ifBlock = 2
    RULE_whileBlock = 3
    RULE_block = 4
    RULE_assignment = 5
    RULE_expr = 6
    RULE_compareOp = 7
    RULE_constant = 8

    ruleNames =  [ "prog", "stat", "ifBlock", "whileBlock", "block", "assignment", 
                   "expr", "compareOp", "constant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    MUL=18
    DIV=19
    ADD=20
    SUB=21
    ID=22
    INT=23
    STRING=24
    BOOLEAN=25
    FLOAT=26
    NULL=27
    NEWLINE=28
    COMMENT=29
    WS=30
    INVALID_CHAR=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MiniLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stat()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2420113570) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifBlock(self):
            return self.getTypedRuleContext(MiniLangParser.IfBlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class UnrecognizedTokenContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INVALID_CHAR(self):
            return self.getToken(MiniLangParser.INVALID_CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnrecognizedToken" ):
                listener.enterUnrecognizedToken(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnrecognizedToken" ):
                listener.exitUnrecognizedToken(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnrecognizedToken" ):
                return visitor.visitUnrecognizedToken(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(MiniLangParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileBlock(self):
            return self.getTypedRuleContext(MiniLangParser.WhileBlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(MiniLangParser.T__0)
                self.state = 24
                self.match(MiniLangParser.T__1)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(MiniLangParser.T__2)
                self.state = 27
                self.match(MiniLangParser.T__3)
                pass
            elif token in [22]:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.assignment()
                self.state = 30
                self.match(MiniLangParser.T__3)
                pass
            elif token in [5]:
                localctx = MiniLangParser.IfStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.ifBlock()
                pass
            elif token in [7]:
                localctx = MiniLangParser.WhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.whileBlock()
                pass
            elif token in [28]:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.match(MiniLangParser.NEWLINE)
                pass
            elif token in [31]:
                localctx = MiniLangParser.UnrecognizedTokenContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.match(MiniLangParser.INVALID_CHAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.BlockContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = MiniLangParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MiniLangParser.T__4)
            self.state = 39
            self.expr(0)
            self.state = 40
            self.block()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 41
                self.match(MiniLangParser.T__5)
                self.state = 42
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_whileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlock" ):
                listener.enterWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlock" ):
                listener.exitWhileBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlock" ):
                return visitor.visitWhileBlock(self)
            else:
                return visitor.visitChildren(self)




    def whileBlock(self):

        localctx = MiniLangParser.WhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MiniLangParser.T__6)
            self.state = 46
            self.expr(0)
            self.state = 47
            self.match(MiniLangParser.T__7)
            self.state = 48
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MiniLangParser.T__8)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2420113570) != 0):
                self.state = 51
                self.stat()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(MiniLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MiniLangParser.ID)
            self.state = 60
            self.match(MiniLangParser.T__10)
            self.state = 61
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def compareOp(self):
            return self.getTypedRuleContext(MiniLangParser.CompareOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ConstantExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(MiniLangParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpr" ):
                listener.enterConstantExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpr" ):
                listener.exitConstantExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantExpr" ):
                return visitor.visitConstantExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 26, 27]:
                localctx = MiniLangParser.ConstantExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.constant()
                pass
            elif token in [22]:
                localctx = MiniLangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(MiniLangParser.ID)
                pass
            elif token in [2]:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(MiniLangParser.T__1)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(MiniLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 76
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.CompareContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 79
                        self.compareOp()
                        self.state = 80
                        self.expr(2)
                        pass

             
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompareOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_compareOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareOp" ):
                listener.enterCompareOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareOp" ):
                listener.exitCompareOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOp" ):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)




    def compareOp(self):

        localctx = MiniLangParser.CompareOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compareOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def STRING(self):
            return self.getToken(MiniLangParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniLangParser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MiniLangParser.FLOAT, 0)

        def NULL(self):
            return self.getToken(MiniLangParser.NULL, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = MiniLangParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 260046848) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         





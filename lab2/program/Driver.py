import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor
from antlr4.error.ErrorListener import ErrorListener


class MiniLangErrorListener(ErrorListener):
    def __init__(self):
        super(MiniLangErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax Error: {msg} at line {line}, column {column}")

class MiniLangCustomVisitor(MiniLangVisitor):
    def __init__(self):
        self.memory = {}  # To store variable assignments

    def visitProg(self, ctx: MiniLangParser.ProgContext):
        return self.visitChildren(ctx)

    def visitPrintExpr(self, ctx: MiniLangParser.PrintExprContext):
        value = self.visit(ctx.expr())

        if value is None:
            print(f"Error: Invalid value for print statement")
            return  
        
        print(value)
        return value

    def visitAssignment(self, ctx: MiniLangParser.AssignmentContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())  
        self.memory[id] = value
        return value
    
    def visitIfBlock(self, ctx: MiniLangParser.IfBlockContext):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.block(1) is not None:
            self.visit(ctx.block(1))
        
    def visitBlock(self, ctx: MiniLangParser.BlockContext):
        return self.visitChildren(ctx)
    
    def visitCompare(self, ctx: MiniLangParser.CompareContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '<=':
            return left <= right
        elif op == '>':
            return left > right
        elif op == '>=':
            return left >= right
        
    def visitWhileBlock(self, ctx: MiniLangParser.WhileBlockContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.block())

    def visitMulDiv(self, ctx: MiniLangParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).symbol.type == MiniLangParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx: MiniLangParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).symbol.type == MiniLangParser.ADD:
            return left + right
        else:
            return left - right

    def visitInt(self, ctx: MiniLangParser.IntContext):
        return int(ctx.INT().getText())
    
    def visitConstant(self, ctx: MiniLangParser.ConstantContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        return None

    def visitId(self, ctx: MiniLangParser.IdContext):
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        return 0  # Default value if variable not found

    def visitParens(self, ctx: MiniLangParser.ParensContext):
        return self.visit(ctx.expr())

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!
    
    visitor = MiniLangCustomVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)

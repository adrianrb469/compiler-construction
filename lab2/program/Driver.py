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
        if op == "==":
            return left == right
        elif op == "!=":
            return left != right
        elif op == "<":
            return left < right
        elif op == "<=":
            return left <= right
        elif op == ">":
            return left > right
        elif op == ">=":
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

        operator = ctx.getChild(1).symbol.type

        if type(left) == int and type(right) == float:
            if operator == MiniLangParser.ADD:
                return left + right
            elif operator == MiniLangParser.SUB:
                return left - right

        if type(left) == float and type(right) == int:
            if operator == MiniLangParser.ADD:
                return left + right
            elif operator == MiniLangParser.SUB:
                return left - right

        if type(left) == int and type(right) == int:
            if operator == MiniLangParser.ADD:
                return left + right
            elif operator == MiniLangParser.SUB:
                return left - right

        raise Exception(f"Cannot add {type(left).__name__} and {type(right).__name__}")

    def visitConstant(self, ctx: MiniLangParser.ConstantContext):
        if ctx.INT():
            return int(ctx.INT().getText())

        if ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == "true"

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.NULL():
            return None

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        raise Exception(f"Invalid constant: {ctx.getText()}")

    def visitId(self, ctx: MiniLangParser.IdContext):
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        else:
            raise Exception(f"Undefined variable: {id}")

    def visitParens(self, ctx: MiniLangParser.ParensContext):
        return self.visit(ctx.expr())

class EvalVisitor(MiniLangVisitor):

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if ctx.EQ():
            return left == right
        elif ctx.NEQ():
            return left != right
        elif ctx.LT():
            return left < right
        elif ctx.GT():
            return left > right
        elif ctx.LTE():
            return left <= right
        elif ctx.GTE():
            return left >= right
        else:
            raise Exception("Unknown comparison operator")

    # Ensure visitExpression can handle comparisonExpr
    def visitExpression(self, ctx):
        if ctx.comparisonExpr():
            return self.visitComparisonExpr(ctx.comparisonExpr())
        else:
            # Handle other expression types
            # TODO Implement handling of other expression types
            return self.visitChildren(ctx)


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = (
        parser.prog()
    )  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!

    visitor = MiniLangCustomVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main(sys.argv)

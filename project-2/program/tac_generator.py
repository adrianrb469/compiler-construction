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
        return self.visitChildren(ctx)

    def visitComparison(self, ctx: CompiscriptParser.ComparisonContext):
        return self.visitChildren(ctx)

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

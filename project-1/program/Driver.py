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


class ObjectInstance:
    def __init__(self, class_symbol: ClassSymbol):
        self.class_symbol = class_symbol
        self.data_type = DataType.OBJECT

    def to_dict(self):
        return {
            "type": "ObjectInstance",
            "class": self.class_symbol.name,
            "data_type": self.data_type.name,
        }


class CompiscriptCompiler(CompiscriptVisitor):
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.current_class = None
        self.current_function = None
        self.errors: List[str] = []
        self.loop_depth = 0
        self.in_init = False  # New flag to track if we're inside an init method
        self.anon_function_counter = 0

    def visit(self, tree):
        if tree is None:
            print("Error: Attempting to visit None")
            return DataType.ANY
        try:
            return super().visit(tree)
        except Exception as e:
            print(f"Error during visit: {e}")
            return DataType.ANY

    def report_error(self, message: str, ctx):
        line = ctx.start.line
        column = ctx.start.column
        print(f"Error at line {line}, column {column}: {message}")
        self.errors.append(f"Error at line {line}, column {column}: {message}")

    def visitProgram(self, ctx: CompiscriptParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visit(declaration)

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

        new_class = self.symbol_table.declare_symbol(
            class_name,
            SymbolType.CLASS,
            DataType.OBJECT,
            ctx.start.line,
            ctx.start.column,
        )

        assert isinstance(new_class, ClassSymbol)

        parent_class = None

        # Inheritance
        if ctx.IDENTIFIER(1):
            parent_class_name = ctx.IDENTIFIER(1).getText()
            parent_class = self.symbol_table.lookup(parent_class_name)
            if not parent_class:
                self.report_error(f"Class '{parent_class_name}' not defined", ctx)
                return None
            if not isinstance(parent_class, ClassSymbol):
                self.report_error(f"'{parent_class_name}' is not a class", ctx)
                return None

            new_class.superclass = parent_class

        # Enter the class scope
        self.symbol_table.enter_scope(class_name)
        self.current_class = new_class

        if parent_class:
            new_class.inherit(parent_class)

        # Visit all functions in the class
        functions_ctx = ctx.functions()
        if functions_ctx:
            for function_ctx in functions_ctx.function():
                self.visit(function_ctx)

        # Exit the class scope
        self.symbol_table.exit_scope()
        self.current_class = None

        return None

    # def visitInit(self, ctx: CompiscriptParser.InitContext):
    #     # verify that the initializer is in a class context
    #     if not self.current_class:
    #         self.report_error("Initializer outside of class context", ctx)
    #         return None

    #     fun_symbol = self.symbol_table.declare_symbol(
    #         "init",
    #         SymbolType.FUNCTION,
    #         DataType.VOID,
    #         ctx.start.line,
    #         ctx.start.column,
    #     )

    #     self.current_function = fun_symbol

    #     # Get the initializer name as this.attribute = value
    #     self.current_class.methods["init"] = fun_symbol

    #     self.symbol_table.enter_scope("init")

    #     if ctx.parameters():
    #         print("visiting parameters")
    #         self.visit(ctx.parameters())

    #     self.visit(ctx.block())

    #     self.symbol_table.exit_scope()
    #     self.current_function = None

    def visitFunDecl(self, ctx: CompiscriptParser.FunDeclContext):
        return self.visit(ctx.function())

    def visitVarDecl(self, ctx: CompiscriptParser.VarDeclContext):
        var_name = ctx.IDENTIFIER().getText()

        if self.symbol_table.lookup(var_name, current_scope_only=True):
            self.report_error(f"Variable '{var_name}' already defined", ctx)
            return None

        if ctx.expression():
            expr_result = self.visit(ctx.expression())
            if isinstance(expr_result, FunctionSymbol):
                # if the symbol is void, we can't assign it to a variable
                if expr_result.data_type == DataType.VOID:
                    self.report_error(
                        f"Function '{expr_result.name}' returns void, cannot assign to variable",
                        ctx.expression(),
                    )
                    return None

                data_type = expr_result.data_type
                # data_type = DataType.FUNCTION
            elif isinstance(expr_result, tuple) and expr_result[0] == DataType.OBJECT:
                data_type, class_name = expr_result
            else:
                data_type = expr_result

            symbol = self.symbol_table.declare_symbol(
                var_name,
                SymbolType.VARIABLE,
                data_type,
                ctx.start.line,
                ctx.start.column,
            )

            if isinstance(expr_result, FunctionSymbol):
                symbol.value = expr_result

            if isinstance(expr_result, tuple) and expr_result[0] == DataType.OBJECT:
                symbol.attributes["class_name"] = class_name
        else:
            self.symbol_table.declare_symbol(
                var_name,
                SymbolType.VARIABLE,
                DataType.NIL,
                ctx.start.line,
                ctx.start.column,
            )
        return None

    def infer_function_return_type(self, ctx):
        return_types = set()

        def visit_node(node):
            if isinstance(node, CompiscriptParser.ReturnStmtContext):
                if node.expression():
                    return_type = self.visit(node.expression())
                    if isinstance(return_type, UnionType):
                        return_types.update(return_type.types)
                    else:
                        return_types.add(return_type)
            if hasattr(node, "getChildren"):
                for child in node.getChildren():
                    visit_node(child)

        visit_node(ctx)

        if not return_types:
            return DataType.VOID
        elif len(return_types) == 1:
            return next(iter(return_types))
        else:
            print(return_types)
            return UnionType(return_types)

    def visitFunction(self, ctx: CompiscriptParser.FunctionContext):
        fun_name = ctx.IDENTIFIER().getText()
        is_init = fun_name == "init"

        if self.current_class:

            fun_symbol = FunctionSymbol(
                fun_name,
                DataType.ANY,
                ctx.start.line,
                ctx.start.column,
            )
            self.current_class.methods[fun_name] = fun_symbol
        else:
            # If we're not in a class, declare the function in the current scope
            if self.symbol_table.lookup(fun_name, current_scope_only=True):
                self.report_error(f"Function '{fun_name}' already defined", ctx)
                return None
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

        if is_init:
            self.in_init = True

        # Process parameters
        if ctx.parameters():
            self.visit(ctx.parameters())

        # Visit the function body
        self.visit(ctx.block())

        # Finalize the return type
        fun_symbol.finalize_return_type()

        self.symbol_table.exit_scope()
        self.current_function = None

        if is_init:
            self.in_init = False

        return fun_symbol

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
            return_value = self.visit(ctx.expression())

            # Handle returning a function
            if isinstance(return_value, FunctionSymbol):
                self.current_function.add_return_type(DataType.FUNCTION)
            else:
                self.current_function.add_return_type(return_value)
        else:
            self.current_function.add_return_type(DataType.VOID)

        return None

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

            self.report_error("'break' statement outside of loop", ctx)
        return None

    def visitContinueStmt(self, ctx: CompiscriptParser.ContinueStmtContext):
        if self.loop_depth == 0:
            self.report_error("'continue' statement outside of loop", ctx)
        return None

    def visitBlock(self, ctx: CompiscriptParser.BlockContext):
        # Check if this block is a standalone block statement
        is_standalone_block = isinstance(
            ctx.parentCtx, CompiscriptParser.StatementContext
        )

        if is_standalone_block:
            self.symbol_table.enter_scope("block")

        for declaration in ctx.declaration():
            self.visit(declaration)

        if is_standalone_block:
            self.symbol_table.exit_scope()

        return None

    def visitFunAnon(self, ctx: CompiscriptParser.FunAnonContext):
        fun_name = self.generate_anon_function_name()

        # Create a new FunctionSymbol for the anonymous function
        fun_symbol = self.symbol_table.declare_symbol(
            fun_name,
            SymbolType.FUNCTION,
            DataType.FUNCTION,
            ctx.start.line,
            ctx.start.column,
        )
        assert isinstance(fun_symbol, FunctionSymbol)

        # Save the current function and set the anonymous function as the current one
        outer_function = self.current_function
        self.current_function = fun_symbol

        # Create a new scope for the anonymous function
        self.symbol_table.enter_scope(fun_name)

        # Process parameters
        if ctx.parameters():
            self.visit(ctx.parameters())

        # Visit the function body
        self.visit(ctx.block())

        # Finalize the return type
        fun_symbol.finalize_return_type()

        # Exit the anonymous function scope
        self.symbol_table.exit_scope()

        # Restore the outer function as the current one
        self.current_function = outer_function

        return fun_symbol

    def generate_anon_function_name(self):
        self.anon_function_counter += 1
        return f"anon_fun_{self.anon_function_counter}"

    def visitExpression(self, ctx: CompiscriptParser.ExpressionContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.funAnon():
            return self.visit(ctx.funAnon())
        return DataType.ANY

    def are_types_compatible(self, expected: DataType, actual: DataType):
        if expected == DataType.ANY or actual == DataType.ANY:
            return True
        return expected == actual

    def visitAssignment(self, ctx: CompiscriptParser.AssignmentContext):

        # this. in init method have to be handled differently,
        # they create a new property in the current class and assign it a value
        if (
            ctx.call()
            and ctx.call().primary()
            and ctx.call().primary().getText() == "this"
            and self.in_init
            and ctx.IDENTIFIER()
        ):
            # Handle 'this.' assignment in init method
            if not self.current_class:
                self.report_error("'this' used outside of class context", ctx)
                return DataType.ANY

            property_name = ctx.IDENTIFIER().getText()
            expr_type = self.visit(
                ctx.assignment() if ctx.assignment() else ctx.logicOr()
            )

            # Check if the property is already defined in the current class
            if self.current_class.get_field(property_name):
                self.report_error(
                    f"Property '{property_name}' already defined in class '{self.current_class.name}'",
                    ctx,
                )
                return DataType.ANY

            # Add the property to the current class
            self.current_class.add_field(
                Symbol(
                    property_name,
                    SymbolType.VARIABLE,
                    expr_type,
                    ctx.start.line,
                    ctx.start.column,
                )
            )

            # ? Should we declare the property as a symbol in the symbol table?
            self.symbol_table.declare_symbol(
                property_name,
                SymbolType.VARIABLE,
                expr_type,
                ctx.start.line,
                ctx.start.column,
            )
            return expr_type

        # Handle regular this.var = value assignments
        if (
            ctx.call()
            and ctx.call().primary()
            and ctx.call().primary().getText() == "this"
        ):
            # To handle this, we just have to check if we're in a class context,
            # then check if the property exists in the class
            # and finally check if the assignment is valid
            if not self.current_class:
                self.report_error("'this' used outside of class context", ctx)
                return DataType.ANY

            property_name = ctx.IDENTIFIER().getText()
            symbol = self.current_class.get_field(property_name)
            if not symbol:

                self.report_error(
                    f"Property '{property_name}' not defined in class '{self.current_class.name}'",
                    ctx,
                )
                return DataType.ANY

            expr_type = self.visit(
                ctx.assignment() if ctx.assignment() else ctx.logicOr()
            )
            if not self.are_types_compatible(symbol.data_type, expr_type):
                self.report_error(
                    f"Type mismatch in assignment to '{property_name}', expected {symbol.data_type} but got {expr_type}",
                    ctx,
                )
                return DataType.ANY

            return expr_type

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

            # If either operand is a string, the operation must be concatenation
            # but also it can only be a number, string or boolean

            if left == DataType.STRING or right == DataType.STRING:
                if op != "+":
                    self.report_error(f"Invalid operation '{op}' on strings", ctx)
                    return DataType.ANY
                if left not in [
                    DataType.STRING,
                    DataType.INT,
                    DataType.FLOAT,
                ] or right not in [DataType.STRING, DataType.INT, DataType.FLOAT]:
                    self.report_error(
                        f"Invalid types for string concatenation: {left.name} and {right.name}",
                        ctx,
                    )
                    return DataType.ANY
                return DataType.STRING

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
        class_name = ctx.IDENTIFIER().getText()
        class_symbol = self.symbol_table.lookup(class_name)

        if not class_symbol or not isinstance(class_symbol, ClassSymbol):
            self.report_error(f"Class '{class_name}' not defined", ctx)
            return DataType.ANY

        print(f"Class symbol: {class_symbol}")

        # Check if the class has an init method
        init_method = class_symbol.get_method("init")
        if init_method:
            print(f"Found init method for class '{class_name}'")
            # Check if the number of arguments matches the init method's parameters
            if ctx.arguments():
                arg_count = len(ctx.arguments().expression())
                if arg_count != len(init_method.parameters):
                    self.report_error(
                        f"Constructor for '{class_name}' expects {len(init_method.parameters)} arguments, but got {arg_count}",
                        ctx,
                    )
            elif len(init_method.parameters) > 0:
                self.report_error(
                    f"Constructor for '{class_name}' expects {len(init_method.parameters)} arguments, but got 0",
                    ctx,
                )

        # Visit arguments if any
        if ctx.arguments():
            self.visit(ctx.arguments())

        print(f"Instantiated class '{class_name}'")
        return (DataType.OBJECT, class_name)

    # Helper functions for call handling

    def validate_arguments(
        self, func_symbol: FunctionSymbol, args: List[DataType], ctx
    ):

        def are_types_compatible(self, expected: DataType, actual: DataType):
            if expected == DataType.ANY or actual == DataType.ANY:
                return True
            return expected == actual

        # The obvious case first, mismatch in number of arguments
        if len(args) != len(func_symbol.parameters):
            self.report_error(
                f"Expected {len(func_symbol.parameters)} arguments, but got {len(args)}",
                ctx,
            )
            return False

        # Now, we need to check if the types of the arguments match the expected types
        for i, (param, arg) in enumerate(zip(func_symbol.parameters, args)):
            if not self.are_types_compatible(param.data_type, arg):
                self.report_error(
                    f"Argument {i+1} type mismatch. Expected {param.data_type}, but got {arg}",
                    ctx,
                )
                return False

        return True

    def visitCall(self, ctx: CompiscriptParser.CallContext):
        if ctx is None:
            print("Error: ctx is None in visitCall")
            return DataType.ANY

        if ctx.primary() is None:
            print("Error: ctx.primary() is None in visitCall")
            return DataType.ANY

        result = self.visit(ctx.primary())
        if result is None:
            print(
                f"Warning: visit(ctx.primary()) returned None for {ctx.primary().getText()}"
            )
            result = DataType.ANY

        for i in range(1, len(ctx.children) - 1, 2):
            child = ctx.getChild(i)
            if child is None:
                print(f"Error: child at index {i} is None in visitCall")
                continue

            if child.getText() == "(":
                # Function call
                primary = ctx.primary()
                is_super_call = False
                function_name = primary.getText()

                # Check if it's a method call on super
                if (
                    isinstance(primary, CompiscriptParser.PrimaryContext)
                    and primary.getChildCount() > 1
                ):
                    if (
                        primary.getChild(0).getText() == "super"
                        and primary.getChild(1).getText() == "."
                    ):
                        is_super_call = True
                        function_name = primary.getChild(2).getText()

                arguments = []
                if i + 1 < len(ctx.children) and isinstance(
                    ctx.getChild(i + 1), CompiscriptParser.ArgumentsContext
                ):
                    args_ctx = ctx.getChild(i + 1)
                    for arg in args_ctx.expression():
                        arg_result = self.visit(arg)
                        if arg_result is None:
                            print(
                                f"Warning: visit(arg) returned None for argument {arg.getText()}"
                            )
                            arg_result = DataType.ANY
                        arguments.append(arg_result)

                function = None

                if is_super_call:
                    if not self.current_class:
                        self.report_error(
                            "Attempt to call 'super' outside of class context", ctx
                        )
                        return DataType.ANY
                    if self.current_class.superclass is None:
                        self.report_error(
                            f"Class '{self.current_class.name}' does not have a parent class",
                            ctx,
                        )
                        return DataType.ANY

                    symbol = self.symbol_table.lookup(self.current_class.superclass)

                    if not isinstance(symbol, ClassSymbol):
                        self.report_error(
                            f"Superclass '{self.current_class.superclass}' not found",
                            ctx,
                        )
                        return DataType.ANY

                    parent_function = symbol.get_method(function_name)

                    if not parent_function:
                        self.report_error(
                            f"Parent class '{self.current_class.superclass}' has no function '{function_name}'",
                            ctx,
                        )
                        return DataType.ANY
                    function = parent_function
                else:
                    if isinstance(result, FunctionSymbol):
                        # This is a stored function or an anonymous function, we need to call it
                        function = result
                    else:
                        symbol = self.symbol_table.lookup(function_name)
                        if symbol is None:
                            self.report_error(
                                f"Function '{function_name}' not defined", ctx
                            )
                            return DataType.ANY

                        if symbol.data_type == DataType.OBJECT:
                            class_name = symbol.attributes["class_name"]
                            class_symbol = self.symbol_table.lookup(class_name)
                            if not isinstance(class_symbol, ClassSymbol):
                                self.report_error(
                                    f"Class '{class_name}' not found", ctx
                                )
                                return DataType.ANY
                            symbol = class_symbol.get_method(function_name)
                        elif symbol.data_type == DataType.FUNCTION:
                            # This is a stored function, we need to call it
                            if isinstance(symbol.value, FunctionSymbol):
                                function = symbol.value
                            else:
                                self.report_error(
                                    f"'{function_name}' is not callable", ctx
                                )
                                return DataType.ANY
                        elif not isinstance(symbol, FunctionSymbol):
                            self.report_error(
                                f"'{function_name}' is not a function", ctx
                            )
                            return DataType.ANY

                        if function is None:
                            function = symbol

                if function is not None:
                    if not self.validate_arguments(function, arguments, ctx):
                        return DataType.ANY
                    result = function.data_type

            elif child.getText() == ".":
                # Property access
                property_name = ctx.getChild(i + 1).getText()
                is_method_call = (
                    i + 2 < len(ctx.children) and ctx.getChild(i + 2).getText() == "("
                )

                if isinstance(result, ClassSymbol):
                    # Static property or method access
                    if property_name in result.methods:
                        result = result.methods[property_name]
                    elif property_name in result.fields:
                        result = result.fields[property_name]
                    else:
                        self.report_error(
                            f"'{property_name}' is not a member of class '{result.name}'",
                            ctx,
                        )
                        return DataType.ANY
                elif result == DataType.OBJECT:
                    # Instance property or method access
                    if ctx.primary().getText() == "this":
                        if not self.current_class:
                            self.report_error(
                                "'this' used outside of class context", ctx
                            )
                            return DataType.ANY
                        class_symbol = self.current_class
                    elif ctx.primary().getText() == "super":
                        if not self.current_class:
                            self.report_error(
                                "'super' used outside of class context", ctx
                            )
                            return DataType.ANY
                        if not self.current_class.superclass:
                            self.report_error(
                                f"Class '{self.current_class.name}' does not have a parent class",
                                ctx,
                            )
                            return DataType.ANY
                        class_symbol = self.symbol_table.lookup(
                            self.current_class.superclass
                        )
                        if not isinstance(class_symbol, ClassSymbol):
                            self.report_error(
                                f"Superclass '{self.current_class.superclass}' not found",
                                ctx,
                            )
                            return DataType.ANY
                    else:
                        instance_symbol = self.symbol_table.lookup(
                            ctx.primary().getText()
                        )
                        if (
                            instance_symbol
                            and "class_name" in instance_symbol.attributes
                        ):
                            class_name = instance_symbol.attributes["class_name"]
                            class_symbol = self.symbol_table.lookup(class_name)
                            if not isinstance(class_symbol, ClassSymbol):
                                self.report_error(
                                    f"Class '{class_name}' not found", ctx
                                )
                                return DataType.ANY
                        else:
                            self.report_error("Cannot determine class of object", ctx)
                            return DataType.ANY

                    method = class_symbol.get_method(property_name)
                    field = class_symbol.get_field(property_name)

                    if method and field:
                        self.report_error(
                            f"Ambiguous reference to '{property_name}' in class '{class_symbol.name}': both method and field exist",
                            ctx,
                        )
                        return DataType.ANY
                    elif method:
                        if not is_method_call:
                            self.report_error(
                                f"'{property_name}' is a method but it's being accessed as a property",
                                ctx,
                            )
                            return DataType.ANY
                        result = method
                    elif field:
                        if is_method_call:
                            self.report_error(
                                f"'{property_name}' is a property but it's being called as a method",
                                ctx,
                            )
                            return DataType.ANY
                        result = field.data_type
                    else:
                        self.report_error(
                            f"'{property_name}' is not defined in class '{class_symbol.name}'",
                            ctx,
                        )
                        return DataType.ANY
            elif child.getText() == "[":
                # Array indexing
                index_expr = ctx.getChild(i + 1)
                index_type = self.visit(index_expr)
                if index_type != DataType.INT:
                    self.report_error("Array index must be an integer", ctx)
                    return DataType.ANY
                if result != DataType.ARRAY:
                    self.report_error("Indexing is only allowed on arrays", ctx)
                    return DataType.ANY
                # For simplicity, we assume all array elements are of type ANY
                result = DataType.ANY

        if ctx.funAnon():
            anon_result = self.visit(ctx.funAnon())
            if anon_result is None:
                print("Warning: visit(ctx.funAnon()) returned None")
                return DataType.ANY
            return anon_result

        return result

    def get_instance_class(self, primary_ctx):
        if isinstance(primary_ctx, CompiscriptParser.PrimaryContext):
            if primary_ctx.IDENTIFIER():
                var_name = primary_ctx.IDENTIFIER().getText()
                symbol = self.symbol_table.lookup(var_name)

                print("Symbol: ", symbol.data_type)
                if isinstance(symbol, ClassSymbol):
                    return symbol
        return None

    def visitPrimary(self, ctx: CompiscriptParser.PrimaryContext):
        if ctx.NUMBER():
            return DataType.FLOAT if "." in ctx.NUMBER().getText() else DataType.INT
        elif ctx.STRING():
            return DataType.STRING

        elif ctx.getChild(0).getText() == "super":
            if not self.current_class:
                self.report_error("'super' used outside of class context", ctx)
                return DataType.ANY
            if not self.current_class.superclass:
                self.report_error(
                    f"Class '{self.current_class.name}' does not have a parent class",
                    ctx,
                )
                return DataType.ANY

            identifier = ctx.IDENTIFIER().getText()
            superclass_symbol = self.symbol_table.lookup(self.current_class.superclass)

            if not isinstance(superclass_symbol, ClassSymbol):
                self.report_error(
                    f"Superclass '{self.current_class.superclass}' not found or not a class",
                    ctx,
                )
                return DataType.ANY

            # Check if it's a method or a field
            method = superclass_symbol.get_method(identifier)
            if method:
                return method.data_type

            field = superclass_symbol.get_field(identifier)
            if field:
                return field.data_type

            self.report_error(
                f"'{identifier}' not found in superclass '{self.current_class.superclass}'",
                ctx,
            )
            return DataType.ANY
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            print("Var name: ", var_name)
            symbol = self.symbol_table.lookup(var_name)

            print("Symbol: ", symbol)
            if not symbol:
                self.report_error(f"!! Variable '{var_name}' not defined", ctx)
                return DataType.ANY
            return symbol.data_type
        elif ctx.getChild(0).getText() in ["true", "false"]:
            return DataType.BOOLEAN
        elif ctx.getChild(0).getText() == "nil":
            return DataType.NULL
        elif ctx.getChild(0).getText() == "this":
            if not self.current_class:
                self.report_error("'this' used outside of class context", ctx)
            return DataType.OBJECT
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.array():
            return DataType.ARRAY
        elif ctx.instantiation():
            return self.visit(ctx.instantiation())
        else:
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
                print(
                    "Adding parameter to current function ", self.current_function.name
                )
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
        import traceback

        error_type = type(e).__name__
        error_message = str(e)
        tb = traceback.extract_tb(e.__traceback__)
        filename, line_number, func_name, text = tb[-1]
        error_location = f"File {filename}, line {line_number}, in {func_name}"
        full_error_message = f"{error_type} at {error_location}: {error_message}"
        print("Error compiling code:", full_error_message)
        return None, [full_error_message], None

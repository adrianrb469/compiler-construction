from enum import Enum, auto
from typing import Dict, Any, Optional, List, Union


class SymbolType(Enum):
    CLASS = auto()
    FUNCTION = auto()
    VARIABLE = auto()


class DataType(Enum):
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()
    ARRAY = auto()
    OBJECT = auto()
    ANY = auto()
    VOID = auto()


class Symbol:
    def __init__(
        self,
        name: str,
        symbol_type: SymbolType,
        data_type: DataType,
        line: int,
        column: int,
    ):
        self.name = name
        self.symbol_type = symbol_type
        self.data_type = data_type
        self.line = line
        self.column = column
        self.value: Any = None
        self.attributes: Dict[str, Any] = {}


class ClassSymbol(Symbol):
    def __init__(
        self, name: str, line: int, column: int, superclass: Optional[str] = None
    ):
        super().__init__(name, SymbolType.CLASS, DataType.OBJECT, line, column)
        self.superclass = superclass
        self.methods: Dict[str, "FunctionSymbol"] = {}
        self.fields: Dict[str, Symbol] = {}


class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: DataType, line: int, column: int):
        super().__init__(name, SymbolType.FUNCTION, return_type, line, column)
        self.parameters: List[Symbol] = []


class SymbolTable:
    def __init__(self):
        self.scopes: List[Dict[str, Symbol]] = [{}]
        self.current_scope = 0

    def enter_scope(self):
        self.scopes.append({})
        self.current_scope += 1

    def exit_scope(self):
        if self.current_scope > 0:
            self.scopes.pop()
            self.current_scope -= 1

    def declare(self, symbol: Symbol):
        self.scopes[self.current_scope][symbol.name] = symbol

    def lookup(self, name: str, current_scope: bool = False) -> Optional[Symbol]:
        if current_scope:
            return self.scopes[self.current_scope].get(name, None)

        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def update(self, name: str, value: Any) -> bool:
        symbol = self.lookup(name)
        if symbol:
            symbol.value = value
            return True
        return False

    def get_current_scope(self) -> Dict[str, Symbol]:
        return self.scopes[self.current_scope]

    def declare_symbol(
        self,
        name: str,
        symbol_type: SymbolType,
        data_type: DataType,
        line: int,
        column: int,
    ) -> Symbol:
        symbol: Union[Symbol, ClassSymbol, FunctionSymbol]
        if symbol_type == SymbolType.CLASS:
            symbol = ClassSymbol(name, line, column)
        elif symbol_type == SymbolType.FUNCTION:
            symbol = FunctionSymbol(name, data_type, line, column)
        else:
            symbol = Symbol(name, symbol_type, data_type, line, column)
        self.declare(symbol)
        return symbol

    def add_method_to_class(self, class_name: str, method: FunctionSymbol):
        class_symbol = self.lookup(class_name)
        if isinstance(class_symbol, ClassSymbol):
            class_symbol.methods[method.name] = method

    def add_field_to_class(self, class_name: str, field: Symbol):
        class_symbol = self.lookup(class_name)
        if isinstance(class_symbol, ClassSymbol):
            class_symbol.fields[field.name] = field

from enum import Enum, auto
import json
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
    NULL = auto()


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

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "symbol_type": self.symbol_type.name,
            "data_type": self.data_type.name,
            "line": self.line,
            "column": self.column,
            "value": str(self.value) if self.value is not None else None,
            "attributes": self.attributes,
        }


class ClassSymbol(Symbol):
    def __init__(
        self, name: str, line: int, column: int, superclass: Optional[str] = None
    ):
        super().__init__(name, SymbolType.CLASS, DataType.OBJECT, line, column)
        self.superclass = superclass
        self.methods: Dict[str, "FunctionSymbol"] = {}
        self.fields: Dict[str, Symbol] = {}

    def to_dict(self) -> Dict[str, Any]:
        class_dict = super().to_dict()
        class_dict.update(
            {
                "superclass": self.superclass,
                "methods": {
                    name: method.to_dict() for name, method in self.methods.items()
                },
                "fields": {
                    name: field.to_dict() for name, field in self.fields.items()
                },
            }
        )
        return class_dict


class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: DataType, line: int, column: int):
        super().__init__(name, SymbolType.FUNCTION, return_type, line, column)
        self.parameters: List[Symbol] = []

    def to_dict(self) -> Dict[str, Any]:
        function_dict = super().to_dict()
        function_dict.update(
            {"parameters": [param.to_dict() for param in self.parameters]}
        )
        return function_dict


class Scope:
    def __init__(self, name: str, parent: Optional["Scope"] = None):
        self.name = name
        self.parent = parent
        self.children: List["Scope"] = []
        self.symbols: Dict[str, Symbol] = {}

    def declare(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def lookup(self, name: str, current_scope_only: bool = False) -> Optional[Symbol]:
        if name in self.symbols:
            return self.symbols[name]
        if not current_scope_only and self.parent:
            return self.parent.lookup(name)
        return None

    def update(self, name: str, value: Any) -> bool:
        symbol = self.lookup(name, current_scope_only=True)
        if symbol:
            symbol.value = value
            return True
        if self.parent:
            return self.parent.update(name, value)
        return False

    def get_full_scope_name(self) -> str:
        if self.parent:
            return f"{self.parent.get_full_scope_name()}.{self.name}"
        return self.name

    def __str__(self) -> str:
        return f"Scope(name='{self.name}', symbols={list(self.symbols.keys())})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "symbols": {
                name: symbol.to_dict() for name, symbol in self.symbols.items()
            },
            "children": [child.to_dict() for child in self.children],
        }


class SymbolTable:
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope

    def enter_scope(self, name: str = "") -> Scope:
        new_scope = Scope(
            name=name or f"block_{id(new_scope)}", parent=self.current_scope
        )
        self.current_scope.children.append(new_scope)
        self.current_scope = new_scope
        return new_scope

    def exit_scope(self) -> Optional[Scope]:
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
            return self.current_scope
        return None

    def declare_symbol(
        self,
        name: str,
        symbol_type: SymbolType,
        data_type: DataType,
        line: int,
        column: int,
    ) -> Symbol:
        symbol: Union[Symbol, ClassSymbol, FunctionSymbol]

        match symbol_type:
            case SymbolType.CLASS:
                symbol = ClassSymbol(name, line, column)
            case SymbolType.FUNCTION:
                symbol = FunctionSymbol(name, data_type, line, column)
            case _:
                symbol = Symbol(name, symbol_type, data_type, line, column)

        self.current_scope.declare(symbol)
        return symbol

    def lookup(self, name: str, current_scope_only: bool = False) -> Optional[Symbol]:
        return self.current_scope.lookup(name, current_scope_only)

    def update(self, name: str, value: Any) -> bool:
        return self.current_scope.update(name, value)

    def add_method_to_class(self, class_name: str, method: FunctionSymbol):
        class_symbol = self.lookup(class_name)
        if isinstance(class_symbol, ClassSymbol):
            class_symbol.methods[method.name] = method

    def add_field_to_class(self, class_name: str, field: Symbol):
        class_symbol = self.lookup(class_name)
        if isinstance(class_symbol, ClassSymbol):
            class_symbol.fields[field.name] = field

    def get_current_scope(self) -> Scope:
        return self.current_scope

    def get_scope_name(self) -> str:
        return self.current_scope.name

    def get_full_scope_name(self) -> str:
        return self.current_scope.get_full_scope_name()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "global_scope": self.global_scope.to_dict(),
            "current_scope": self.current_scope.get_full_scope_name(),
        }

    def print_table(self):
        print(json.dumps(self.to_dict(), indent=2))

    def get_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

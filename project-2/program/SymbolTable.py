from enum import Enum, auto
import json
from typing import Dict, Any, Optional, List, Set, Union


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
    NIL = auto()
    UNION = auto()


def get_memory_size(data_type: DataType) -> int:
    """Return the size in bytes of a data type."""
    match data_type:
        case DataType.INT:
            return 4  # 4 bytes for integers
        case DataType.FLOAT:
            return 4  # 4 bytes for floats
        case DataType.BOOLEAN:
            return 1  # 1 byte for booleans
        case DataType.STRING:
            return 8  # 8 bytes for pointers to strings
        case DataType.ARRAY:
            return 8  # Assume arrays are referenced by pointers
        case DataType.OBJECT:
            return 8  # Assume objects are referenced by pointers
        case DataType.ANY:
            return 8  # Treat 'ANY' as a reference type (pointer size, 8 bytes)
        case DataType.UNION:
            # A union would need enough memory to store the largest type
            return max(get_memory_size(t) for t in data_type.types)
        case _:
            return 4  # Default to 4 bytes for other types


class UnionType:
    def __init__(self, types: Set[DataType]):
        self.types = types

    def name(self):
        return f"Union[{', '.join(t.name for t in self.types)}]"

    def __str__(self):
        return f"Union[{', '.join(t.name for t in self.types)}]"


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
        self.offset: Optional[int] = None  # Store the memory offset
        self.size: Optional[int] = None  # Store the memory size in bytes

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "symbol_type": self.symbol_type.name,
            "data_type": (
                self.data_type.name
                if isinstance(self.data_type, DataType)
                else str(self.data_type)
            ),
            "line": self.line,
            "column": self.column,
            "value": str(self.value) if self.value is not None else None,
            "attributes": self.attributes,
            "offset": self.offset,  # Include offset in the output
            "size": self.size,  # Include size in the output
        }


class ClassSymbol(Symbol):
    def __init__(
        self, name: str, line: int, column: int, superclass: Optional[str] = None
    ):
        super().__init__(name, SymbolType.CLASS, DataType.OBJECT, line, column)
        self.superclass = superclass
        self.methods: Dict[str, "FunctionSymbol"] = {}
        self.fields: Dict[str, Symbol] = {}
        self.class_size = 0
        self.current_field_offset = 0

    def inherit(self, parent: "ClassSymbol"):
        """Inherit fields and methods from a parent class."""
        self.superclass = parent.name
        self.methods = parent.methods.copy()
        self.fields = parent.fields.copy()
        self.current_field_offset = (
            parent.class_size
        )  # Start offsets after the parent’s fields
        self.class_size = parent.class_size  # Inherit the parent class size

    def add_field(self, field: Symbol):
        """Add a field to the class, calculate the memory offset, and update class size."""
        size = get_memory_size(field.data_type)  # Get the size of the field
        field.offset = self.current_field_offset  # Set the field's offset
        self.fields[field.name] = field  # Add the field to the class
        self.current_field_offset += size  # Update the offset for the next field
        self.class_size += size  # Update the total size of the class

    def get_field(self, field_name: str) -> Optional[Symbol]:
        return self.fields.get(field_name, None)

    def add_method(self, method: "FunctionSymbol"):
        self.methods[method.name] = method

    def get_method(self, method_name: str) -> Optional["FunctionSymbol"]:
        return self.methods.get(method_name, None)

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
                "class_size": self.class_size,  # Include the total class size
            }
        )
        return class_dict

    def get_method(self, method_name: str) -> Optional["FunctionSymbol"]:
        return self.methods.get(method_name, None)


class FunctionSymbol(Symbol):
    def __init__(
        self,
        name: str,
        return_type: DataType,
        line: int,
        column: int,
        parameters: List[Symbol] = [],
    ):
        super().__init__(name, SymbolType.FUNCTION, return_type, line, column)
        self.parameters: List[Symbol] = []
        self.return_types: Set[DataType] = set()

    def add_return_type(self, return_type: DataType):
        self.return_types.add(return_type)

    def finalize_return_type(self):
        if not self.return_types:
            self.data_type = DataType.VOID
        elif len(self.return_types) == 1:
            self.data_type = next(iter(self.return_types))
        else:
            self.data_type = UnionType(self.return_types)

    def to_dict(self) -> Dict[str, Any]:
        function_dict = super().to_dict()
        function_dict.update(
            {"parameters": [param.to_dict() for param in self.parameters]}
        )
        function_dict["return_types"] = [
            return_type.name for return_type in self.return_types
        ]
        return function_dict


class Scope:
    def __init__(
        self,
        name: str,
        parent: Optional["Scope"] = None,
        unique_id: Optional[int] = None,
    ):
        self.name = name
        self.parent = parent
        self.children: List["Scope"] = []
        self.symbols: Dict[str, Symbol] = {}
        self.current_offset = 0
        self.unique_id = unique_id

    def get_full_scope_name(self) -> str:
        if self.parent:
            return f"{self.parent.get_full_scope_name()}.{self.name}"
        return self.name

    def declare(self, symbol: Symbol):
        size = get_memory_size(symbol.data_type)
        symbol.offset = self.current_offset
        symbol.size = size
        self.current_offset += size
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
        return f"Scope(name='{self.name}', id={self.unique_id}, symbols={list(self.symbols.keys())})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "debug_name": self.get_full_scope_name() + f" ({self.unique_id})",
            "unique_id": self.unique_id,
            "symbols": {
                name: symbol.to_dict() for name, symbol in self.symbols.items()
            },
            "children": [child.to_dict() for child in self.children],
        }


class SymbolTable:
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope
        self.scope_counter = 1
        self.scope_history: List[Scope] = [
            self.global_scope
        ]  # This tracks the entering and exiting of scopes.
        self.id_to_scope: Dict[int, Scope] = {0: self.global_scope}
        self.current_scope_index = 0

    def get_scope_history(self) -> List[Scope]:
        return self.scope_history

    def get_scope_by_id(self, scope_id: int) -> Optional[Scope]:
        return self.id_to_scope.get(scope_id, None)

    def reset_scope(self):
        self.current_scope = self.global_scope

    def next_scope(self) -> Optional[Scope]:
        """Traverse to the next scope in the same order as they were entered."""
        if self.current_scope_index < len(self.scope_history) - 1:
            previous_scope = self.current_scope  # Track the current scope before moving
            self.current_scope_index += 1
            self.current_scope = self.scope_history[self.current_scope_index]

            print(
                f"Moving from scope '{previous_scope.name}' (ID {previous_scope.unique_id}) "
                f"to scope '{self.current_scope.name}' (ID {self.current_scope.unique_id})"
            )

            return self.current_scope
        else:
            print("No more scopes to traverse.")
            return None

    def enter_scope(self, name: str = "") -> Scope:
        if not name:
            # Generate a unique name for anonymous block scopes
            name = f"block_{self.scope_counter}"
        new_scope = Scope(
            name=name, parent=self.current_scope, unique_id=self.scope_counter
        )
        self.scope_counter += 1
        self.current_scope.children.append(new_scope)
        self.current_scope = new_scope
        self.scope_history.append(new_scope)
        self.id_to_scope[new_scope.unique_id] = new_scope
        print(f"Entered new scope: {new_scope.name} with ID {new_scope.unique_id}")
        return new_scope

    def exit_scope(self) -> Optional[Scope]:
        if self.current_scope.parent:
            exited_scope = self.current_scope
            self.current_scope = self.current_scope.parent

            self.scope_history.append(self.current_scope)

            print(f"Exited scope: {exited_scope.name} with ID {exited_scope.unique_id}")
            return self.current_scope
        print("Attempted to exit global scope; operation ignored.")
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
            # Infromation about how scopes were entered and exited, and other
            # information about the scopes
            "scope_history": [scope.to_dict() for scope in self.scope_history],
            "id_to_scope": {
                scope_id: scope.to_dict()
                for scope_id, scope in self.id_to_scope.items()
            },
        }

    def print_table(self):
        print(json.dumps(self.to_dict(), indent=2))

    def get_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def get_class_method(self, class_instance_name:str, method: str):
        # look for the class method in the symbol table and return it
        scope = self.current_scope
        currentClass = scope.symbols.get(class_instance_name)

        if currentClass is None or currentClass.attributes is None:
            return None, None

        classIdentifier = currentClass.attributes['class_name']
        currentClassReference = scope.symbols.get(classIdentifier)

        if currentClassReference is None:
            return None, None

        if isinstance(currentClassReference, ClassSymbol):

            if currentClassReference.get_method(method) is None:
                return None, None

            return currentClassReference, currentClassReference.get_method(method)

        return None, None

    def get_class_field(self, class_instance_name: str, field: str):
        # look for the class attribute (field) & return it
        scope = self.current_scope
        currentClass = scope.symbols.get(class_instance_name)

        if currentClass is None or currentClass.attributes is None:
            return None, None

        classIdentifier = currentClass.attributes['class_name']
        currentClassReference = scope.symbols.get(classIdentifier)

        if currentClassReference is None:
            return None, None

        if isinstance(currentClassReference, ClassSymbol):

            if currentClassReference.get_field(field) is None:
                return None, None

            return currentClassReference, currentClassReference.get_field(field)

        return None, None

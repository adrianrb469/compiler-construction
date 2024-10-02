from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Any, Dict
from SymbolTable import SymbolTable


class Operation(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    ASSIGN = auto()
    GOTO = auto()
    IF = auto()


@dataclass
class Instruction:
    op: Operation
    arg1: Optional[str] = None
    arg2: Optional[str] = None
    result: Optional[str] = None

    def __str__(self):
        parts = [self.op.name]
        if self.arg1 is not None:
            parts.append(str(self.arg1))
        if self.arg2 is not None:
            parts.append(str(self.arg2))
        if self.result is not None:
            parts.append(str(self.result))
        return " ".join(parts)


class IntermediateCodeGenerator:
    def __init__(self, symbol_table: SymbolTable):
        self.code: List[Instruction] = []
        self.temp_count: int = 0
        self.label_count: int = 0
        self.symbol_table: SymbolTable = symbol_table

    def new_temp(self) -> str:
        """Generate a new temporary variable."""
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self) -> str:
        """Generate a new label."""
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(
        self,
        op: Operation,
        arg1: Optional[str] = None,
        arg2: Optional[str] = None,
        result: Optional[str] = None,
    ) -> None:
        """Emit a TAC instruction as an Instruction instance."""
        instruction = Instruction(op=op, arg1=arg1, arg2=arg2, result=result)
        self.code.append(instruction)

    def get_code(self) -> List[Instruction]:
        """Return the list of generated TAC instructions."""
        return self.code

    def print_code(self) -> None:
        """Print the generated TAC in a readable format."""
        for instruction in self.code:
            print(instruction)


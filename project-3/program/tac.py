from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Set


class Operation(Enum):
    # Assignment Operations
    ASSIGN = auto()

    # Arithmetic Operations
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()

    # Logical Operations
    AND = auto()
    OR = auto()
    NOT = auto()
    NEG = auto()

    # Comparison Operations
    EQ = auto()
    NE = auto()
    LT = auto()
    LE = auto()
    GT = auto()
    GE = auto()

    # Control Flow Operations
    GOTO = auto()
    IF_FALSE = auto()
    LABEL = auto()

    # Function and Method Operations
    PARAM = auto()  # For passing parameters
    CALL = auto()  # For calling functions/methods
    RETURN = auto()  # For return statements
    PROCEDURE = auto()  # For procedure declarations
    END_PROCEDURE = auto()  # For procedure terminations

    # Object-Oriented Operations
    INHERIT = auto()  # For class inheritance
    NEW = auto()  # For object instantiation
    LOAD_FIELD = auto()  # For loading a field's value
    LOAD_METHOD = auto()  # For loading a method's address
    STORE_FIELD = auto()  # For storing a value to a field
    ALLOCATE = auto()  # For allocating memory for an object

    # I/O Operations
    PRINT = auto()


@dataclass
class Instruction:
    op: Operation
    arg1: Optional[str] = None
    arg2: Optional[str] = None
    result: Optional[str] = None
    main: Optional[bool] = False

    def __str__(self):
        if self.op == Operation.LABEL:
            return f"{self.result}:"

        if self.op == Operation.PROCEDURE:
            return f"PROC {self.result}:"

        if self.op == Operation.END_PROCEDURE:
            return f"END PROCEDURE"

        if self.op is None:
            return ""

        parts = [self.op.name]
        if self.arg1 is not None:
            parts.append(str(self.arg1))
        if self.arg2 is not None:
            parts.append(str(self.arg2))
        if self.result is not None:
            parts.append(str(self.result))
        return " ".join(parts)  # Add indentation for non-label instructions


class IntermediateCodeGenerator:
    def __init__(self, table):
        self.code: List[Instruction] = []
        self.temp_count: int = 0
        self.label_count: int = 0
        self.table = table

        self.free_temps: List[str] = []
        self.active_temps: Set[str] = set()

    def is_temp(self, var: str) -> bool:
        """Check if a variable name represents a temporary variable."""
        return var.startswith("t")

    def new_temp(self) -> str:
        """Allocate a new temporary variable, reusing from the pool if possible."""
        if self.free_temps:
            temp = self.free_temps.pop()
            self.active_temps.add(temp)
            return temp
        else:
            self.temp_count += 1
            temp = f"t{self.temp_count}"
            self.active_temps.add(temp)
            return temp

    def free_temp(self, temp: str) -> None:
        """Free a temporary variable, making it available for reuse."""
        if temp in self.active_temps:
            self.active_temps.remove(temp)
            self.free_temps.append(temp)
        else:
            raise ValueError(f"Attempting to free unallocated temp: {temp}")

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
        main_code = self.table.current_scope.name == "global"
        instruction = Instruction(
            op=op, arg1=arg1, arg2=arg2, result=result, main=main_code
        )
        self.code.append(instruction)

    def get_code(self) -> List[Instruction]:
        """Return the list of generated TAC instructions."""
        return self.code

    def print_code(self) -> None:
        """Print the generated TAC in a readable format."""
        for instruction in self.code:
            print(instruction)

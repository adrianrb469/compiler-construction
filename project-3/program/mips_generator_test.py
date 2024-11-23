from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Set
from .tac import Instruction, Operation


class MIPSCodeGenerator:
    def __init__(self) -> None:
        self.data_section = [".data"]
        self.text_section = [".text"]

        self.address_table: Dict[str, str] = {}

        self.stack_offset = 0

        self.procedures: Dict[str, List[str]] = {"main": []}
        self.procedure_stack: List[str] = ["main"]

    def emit(self, line: str) -> None:
        self.procedures[self.procedure_stack[-1]].append(line)

    def terminate(self) -> None:
        self.emit("")
        self.emit("li $v0, 10")
        self.emit("syscall")

    def generate(self, instructions: List[Instruction]) -> List[str]:

        for instr in instructions:
            self.evaluate(instr)

        self.terminate()

        formatted_data = [self.data_section[0]]
        for line in self.data_section[1:]:
            formatted_data.append(f"    {line}")

        formatted_text = [self.text_section[0]]

        for procedure in self.procedures:
            if procedure != "main":
                formatted_text.append("")
            else:
                formatted_text.append("main:")

            for line in self.procedures[procedure]:
                if line.endswith(":") or line.startswith("."):
                    formatted_text.append(line)
                else:
                    formatted_text.append(f"    {line}")

        return "\n".join(formatted_data + formatted_text)

    def evaluate(self, instruction: Instruction) -> None:
        match instruction.op:
            case (
                Operation.ADD
                | Operation.SUB
                | Operation.MUL
                | Operation.DIV
                | Operation.MOD
            ):
                self.eval_arithmetic(instruction)
            case Operation.PROCEDURE:
                self.eval_procedure(instruction)
            case Operation.END_PROCEDURE:
                self.end_procedure(instruction)
            case Operation.ASSIGN:
                self.eval_assign(instruction)
            case _:
                print(f"Unknown operation: {instruction.op}")

        pass

    def eval_procedure(self, instr: Instruction) -> None:
        procedure_name = instr.result

        if procedure_name in self.procedures:
            raise ValueError(f"Procedure {procedure_name} already exists")

        self.procedure_stack.append(procedure_name)
        self.procedures[procedure_name] = []
        self.emit(f"{procedure_name}:")

    def end_procedure(self, instr: Instruction) -> None:
        self.emit("jr $ra")
        self.procedure_stack.pop()

    def define_variable(self, var: str, var_type: str = "int") -> None:
        """
        Define a variable by mapping it to a location.

        :param var: Variable name.
        :param var_type: Type of the variable ('int' or 'string').
        """
        if var in self.address_table:
            return  # Variable already defined

        if var.startswith("$"):
            # Variable is a register
            self.address_table[var] = var
            return

        if var_type == "string":
            # Strings are handled in eval_assign
            self.address_table[var] = var  # Will store the address of the string
        else:
            # For integers, map to global memory by default
            self.address_table[var] = var
            self.data_section.append(f"{var}: .word 0")

    def eval_assign(self, instr: Instruction) -> None:
        """Handle assignment operations, including numbers and strings."""
        src = instr.arg1
        dest = instr.result

        # String assignment | assign x "string"
        if src and src.startswith('"') and src.endswith('"'):
            string_content = src[1:-1]
            label = self.get_string_label(string_content)
            self.address_table[dest] = f"{label}"
            self.emit(f"la $t8, {label}")
            self.emit(f"sw $t8, {self.address_table[dest]}")
            return

        # Number assignment | assign x 42
        if src and self.is_numeric(src):
            self.define_variable(dest, var_type="int")
            self.emit(f"li $t8, {src}")
            self.emit(f"sw $t8, {self.address_table[dest]}")
            return

        # Handle variable-to-variable or register-to-variable assignment
        # Resolve source operand
        if self.is_register(src):
            src_loc = src
        else:
            src_loc = self.resolve_operand(src)

        # Map destination variable
        self.define_variable(dest, var_type="int")

        # Perform the assignment
        dest_loc = self.address_table[dest]
        if self.is_register(dest_loc):
            # Destination is a register; use move
            self.emit(f"move {dest_loc}, {src_loc}")
        else:
            # Destination is memory; store the value
            self.emit(f"sw {src_loc}, {dest_loc}")

    def eval_arithmetic(self, instr: Instruction) -> None:
        """Handle arithmetic operations: ADD, SUB, MUL, DIV, MOD."""
        op_map = {
            Operation.ADD: "add",
            Operation.SUB: "sub",
            Operation.MUL: "mul",
            Operation.DIV: "div",
            Operation.MOD: "mod",  # Note: MOD is handled separately
        }

        mips_op = op_map.get(instr.op)
        if not mips_op and instr.op != Operation.MOD:
            raise ValueError(f"Unsupported arithmetic operation: {instr.op}")

        # Handle MOD separately since MIPS uses div and mfhi
        if instr.op == Operation.MOD:
            self.eval_mod(instr)
            return

        # Initialize operand registers
        if instr.arg1 and self.is_numeric(instr.arg1):

            self.emit(f"li $t0, {instr.arg1}")
            operand1 = "$t0"
        else:
            # Operand1 is a register or variable
            operand1 = self.resolve_operand(instr.arg1)

        if instr.arg2 and self.is_numeric(instr.arg2):

            self.emit(f"li $t0, {instr.arg2}")
            operand2 = "$t0"
        else:
            # Operand2 is a register or variable
            operand2 = self.resolve_operand(instr.arg2)

        # Define and map the result variable
        self.define_variable(instr.result, var_type="int")
        result_loc = self.address_table[instr.result]

        # Perform the arithmetic operation
        self.emit(
            f"{mips_op} {result_loc}, {operand1}, {operand2}    # {instr.result} = {instr.arg1} {instr.op.name} {instr.arg2}"
        )

    def eval_mod(self, instr: Instruction) -> None:
        """Handle modulo operation using div and mfhi."""
        # Resolve operands
        operand1 = self.resolve_operand(instr.arg1)
        operand2 = self.resolve_operand(instr.arg2)

        # Perform division
        self.emit(
            f"div {operand1}, {operand2}    # Divide {instr.arg1} by {instr.arg2}"
        )

        # Move the remainder from HI to the result register
        self.define_variable(instr.result, var_type="int")
        result_loc = self.address_table[instr.result]
        self.emit(
            f"mfhi {result_loc}    # {instr.result} = remainder of {instr.arg1} MOD {instr.arg2}"
        )

    def resolve_operand(self, operand: str) -> str:
        """
        Resolve the operand to a register. If it's a variable in memory, load it into a temporary register.
        If its a numeric value, load it into a temporary register.
        :param operand: The operand to resolve.
        :return: The register containing the operand's value.
        """
        if self.is_register(operand):
            return operand
        else:

            var_loc = self.address_table[operand]
            if self.is_register(var_loc):
                return var_loc
            else:
                temp_reg = "$t8"
                self.emit(
                    f"lw {temp_reg}, {var_loc}      # Load {operand} into {temp_reg}"
                )
                return temp_reg

    def is_register(self, var: str) -> bool:
        return var.startswith("$")

    def is_numeric(self, s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    def get_string_label(self, string: str) -> str:
        if string not in self.string_literals:
            label = f"str_{len(self.string_literals)}"
            self.string_literals[string] = label
            # Add the string to the data section with a newline character
            self.data_section.append(f'{label}: .asciiz "{string}\\n"')
        return self.string_literals[string]

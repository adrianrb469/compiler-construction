from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Set
from .tac import Instruction, Operation


class MIPSCodeGenerator:
    def __init__(self) -> None:
        self.registers = [f"$t{i}" for i in range(10)]
        self.register_descriptor: Dict[str, Set[str]] = {
            reg: set() for reg in self.registers
        }
        self.address_descriptor: Dict[str, Set[str]] = {}
        self.data_section: List[str] = [".data"]
        self.text_section: List[str] = [".text", "main:"]
        self.string_literals: Dict[str, str] = {}
        self.stack_offset = 0

    def get_register(self, var: str) -> str:
        """Allocate a register for a variable."""

        # If the variable is already in a register, return the register
        for reg, vars in self.register_descriptor.items():
            if var in vars:
                return reg

        # If the variable is not in a register, assign it to an empty register
        for reg, vars in self.register_descriptor.items():
            if not vars:
                self.register_descriptor[reg].add(var)
                self.address_descriptor.setdefault(var, set()).add(reg)
                return reg

        # At this point, all registers are full, so we need to free one
        reg_to_spill = self.select_register_to_spill()
        self.spill_register(reg_to_spill)
        self.register_descriptor[reg_to_spill].add(var)
        self.address_descriptor.setdefault(var, set()).add(reg_to_spill)

        return reg_to_spill

    def select_register_to_spill(self):
        """Select the first register to spill."""
        for reg, vars in self.register_descriptor.items():
            if vars:
                return reg

    def spill_register(self, reg: str):
        """Spill all variables in a register to memory."""
        vars_to_spill = list(self.register_descriptor[reg])
        for var in vars_to_spill:
            self.text_section.append(
                f"sw {reg}, {self.get_stack_offset(var)}  # Spill {var} to stack"
            )
            self.address_descriptor[var].remove(reg)
            self.address_descriptor[var].add("memory")
        self.register_descriptor[reg].clear()

    def get_stack_offset(self, var: str) -> str:
        if (
            var not in self.address_descriptor
            or "memory" not in self.address_descriptor[var]
        ):
            self.stack_offset += 4  # Increment stack by 4 bytes for each variable
        return f"-{self.stack_offset}($sp)"

    def generate(self, instructions: List[Instruction]) -> str:
        for instr in instructions:
            if instr.op == Operation.ASSIGN:
                self.handle_assign(instr)
            elif instr.op in {
                Operation.ADD,
                Operation.SUB,
                Operation.MUL,
                Operation.DIV,
            }:
                self.handle_arithmetic(instr)
            elif instr.op in {
                Operation.GT,
                Operation.LT,
                Operation.GE,
                Operation.LE,
                Operation.EQ,
                Operation.NE,
            }:
                self.handle_comparison(instr)
            elif instr.op == Operation.IF_FALSE:
                self.handle_if_false(instr)
            elif instr.op == Operation.GOTO:
                self.handle_goto(instr)
            elif instr.op == Operation.LABEL:
                self.handle_label(instr)
            elif instr.op == Operation.PRINT:
                self.handle_print(instr)

        # Add program termination
        program_end = "li $v0, 10  # Syscall to exit\nsyscall"
        return "\n".join(self.data_section + self.text_section + [program_end])

    def handle_assign(self, instr: Instruction):
        if instr.arg1.startswith('"'):  # String literal
            label = self.get_string_literal(instr.arg1)
            reg = self.get_register(instr.result)
            self.text_section.append(
                f"la {reg}, {label}  # {instr.result} = {instr.arg1}"
            )
        elif instr.arg1.isdigit():  # Numeric constant
            reg = self.get_register(instr.result)
            self.text_section.append(
                f"li {reg}, {instr.arg1}  # {instr.result} = {instr.arg1}"
            )
        else:  # Variable/temporary in a register
            src_reg = self.get_register(instr.arg1)
            dest_reg = self.get_register(instr.result)
            self.text_section.append(
                f"move {dest_reg}, {src_reg}  # {instr.result} = {instr.arg1}"
            )

    def handle_arithmetic(self, instr: Instruction):
        reg_result = self.get_register(instr.result)
        op = instr.op
        arg1 = instr.arg1
        arg2 = instr.arg2

        # Determine if arg1 or arg2 is a constant
        if arg1.isdigit():
            # For commutative operations like ADD and MUL, you can swap operands
            if op in {Operation.ADD, Operation.MUL} and arg2.isdigit():
                # Both operands are constants - handle accordingly (possibly optimization)
                # For simplicity, handle one constant at a time
                reg_arg1 = self.get_register(instr.arg1)
                self.text_section.append(
                    f"li {reg_arg1}, {arg1}  # Load constant {arg1}"
                )
                reg_arg2 = self.get_register(instr.arg2)
                self.text_section.append(
                    f"li {reg_arg2}, {arg2}  # Load constant {arg2}"
                )
                self.text_section.append(
                    f"{op_map[op]} {reg_result}, {reg_arg1}, {reg_arg2}  # {instr.result} = {instr.arg1} {op.name.lower()} {instr.arg2}"
                )
                return
            elif op in {Operation.ADD, Operation.SUB}:
                # Use immediate instructions where possible
                reg_arg1 = self.get_register(instr.arg1)
                imm = arg2
                if op == Operation.ADD:
                    self.text_section.append(
                        f"addi {reg_result}, {reg_arg1}, {imm}  # {instr.result} = {instr.arg1} + {imm}"
                    )
                elif op == Operation.SUB:
                    self.text_section.append(
                        f"addi {reg_result}, {reg_arg1}, {-int(imm)}  # {instr.result} = {instr.arg1} - {imm}"
                    )
                return

        elif arg2.isdigit():
            if op in {Operation.ADD, Operation.SUB}:
                reg_arg1 = self.get_register(instr.arg1)
                imm = arg2
                if op == Operation.ADD:
                    self.text_section.append(
                        f"addi {reg_result}, {reg_arg1}, {imm}  # {instr.result} = {instr.arg1} + {imm}"
                    )
                elif op == Operation.SUB:
                    self.text_section.append(
                        f"addi {reg_result}, {reg_arg1}, {-int(imm)}  # {instr.result} = {instr.arg1} - {imm}"
                    )
                return

        # Fallback to register-based instructions
        reg_arg1 = self.get_register(arg1)
        reg_arg2 = self.get_register(arg2)

        op_map = {
            Operation.ADD: "add",
            Operation.SUB: "sub",
            Operation.MUL: "mul",
            Operation.DIV: "div",
        }

        self.text_section.append(
            f"{op_map[op]} {reg_result}, {reg_arg1}, {reg_arg2}  # {instr.result} = {arg1} {op.name.lower()} {arg2}"
        )

    def handle_comparison(self, instr: Instruction):
        reg_result = self.get_register(instr.result)
        reg_arg1 = self.get_register(instr.arg1)

        # Ensure arg2 (a constant) is loaded into a register if needed
        if instr.arg2.isdigit():
            reg_arg2 = self.get_register(instr.arg2)
            self.text_section.append(
                f"li {reg_arg2}, {instr.arg2}  # Load constant {instr.arg2}"
            )
        else:
            reg_arg2 = self.get_register(instr.arg2)

        op_map = {
            Operation.GT: "sgt",
            Operation.LT: "slt",
            Operation.GE: "sge",
            Operation.LE: "sle",
            Operation.EQ: "seq",
            Operation.NE: "sne",
        }
        self.text_section.append(
            f"{op_map[instr.op]} {reg_result}, {reg_arg1}, {reg_arg2}  # {instr.result} = {instr.arg1} {instr.op.name.lower()} {instr.arg2}"
        )

    def handle_if_false(self, instr: Instruction):
        reg = self.get_register(instr.arg1)
        self.text_section.append(
            f"beq {reg}, $zero, {instr.result}  # if not {instr.arg1} goto {instr.result}"
        )

    def handle_goto(self, instr: Instruction):
        self.text_section.append(f"j {instr.result}  # goto {instr.result}")

    def handle_label(self, instr: Instruction):
        self.text_section.append(f"{instr.result}:  # Label {instr.result}")

    def handle_print(self, instr: Instruction):
        if instr.arg1.startswith('"'):  # String literal
            label = self.get_string_literal(instr.arg1)
            self.text_section.append(f"li $v0, 4  # Print string")
            self.text_section.append(f"la $a0, {label}  # Load address of {instr.arg1}")
            self.text_section.append("syscall")
        else:  # Variable (assume numeric for now)
            reg = self.get_register(instr.arg1)
            self.text_section.append(f"li $v0, 1  # Print integer")
            self.text_section.append(f"move $a0, {reg}  # Load value of {instr.arg1}")
            self.text_section.append("syscall")

    def get_string_literal(self, value: str) -> str:
        """Ensure a string literal is in the data section."""
        if value not in self.string_literals:
            label = f"str_{len(self.string_literals)}"
            self.string_literals[value] = label
            self.data_section.append(f"{label}: .asciiz {value}")
        return self.string_literals[value]


instructions = [
    Instruction(op=Operation.ASSIGN, arg1="5", result="x"),
    Instruction(op=Operation.GT, arg1="x", arg2="4", result="t1"),
    Instruction(op=Operation.IF_FALSE, arg1="t1", result="L1"),
    Instruction(op=Operation.PRINT, arg1='"test"'),
    Instruction(op=Operation.GOTO, result="L2"),
    Instruction(op=Operation.LABEL, result="L1"),
    Instruction(op=Operation.ASSIGN, arg1='"string"', result="y"),
    Instruction(op=Operation.LABEL, result="L2"),
]

mips = MIPSCodeGenerator()
mips_code = mips.generate(instructions)

# Save the generated MIPS code to a file
with open("output.s", "w") as f:
    f.write(mips_code)

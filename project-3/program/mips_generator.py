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
        self.variables = set()

        self.procedures = {"main": []}
        self.procedure_stack = ["main"]

        self.current_args = []
        self.current_params = []

    def free_register(self, var: str) -> None:
        """
        Free the register(s) holding the specified variable, excluding 'memory'.
        """

        if var in self.address_descriptor:
            # Create a copy to avoid modifying the set during iteration
            regs = self.address_descriptor[var].copy()

            for reg in regs:
                if reg == "memory":
                    continue  # Skip 'memory' as it's not a register
                if reg in self.register_descriptor:
                    if var in self.register_descriptor[reg]:
                        self.register_descriptor[reg].remove(var)
                # Remove the register from the address descriptor for the variable
                self.address_descriptor[var].remove(reg)
            # If the variable is no longer in any register, remove it from the address descriptor
            if not self.address_descriptor[var]:
                del self.address_descriptor[var]
        else:
            # Variable not found in any register; nothing to free
            pass

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
            self.add_instruction(
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

    def add_instruction(self, instruction: str) -> None:
        """
        Append an instruction to the current procedure.
        """

        current_procedure = self.procedure_stack[-1]
        self.procedures[current_procedure].append(instruction)

    def generate(self, instructions: List[Instruction]) -> str:

        for instr in instructions:
            self.process_instruction(instr)

        # Append termination code to the main text section
        self.add_instruction("li $v0, 10  # Exit syscall")
        self.add_instruction("syscall")

        # Indent the .data section
        indented_data_section = [self.data_section[0]]  # '.data'
        for line in self.data_section[1:]:
            indented_data_section.append(f"    {line}")

        # Initialize the .text section
        text_section = [".text"]

        # Order procedures: main first, then others
        for proc_name in ["main"] + [p for p in self.procedures if p != "main"]:
            if proc_name != "main":
                text_section.append("")  # Blank line for readability
            else:
                text_section.append("main:")

            # Add instructions with proper indentation
            for line in self.procedures[proc_name]:
                if line.endswith(":") or line.startswith("."):
                    text_section.append(line)  # Labels and directives are not indented
                else:
                    text_section.append(f"    {line}")  # Indent instructions

        print("Procedures: ", self.procedures)

        # Combine the .data and .text sections
        final_code = "\n".join(indented_data_section + text_section)
        return final_code

    def process_instruction(self, instr: Instruction):
        print(f"Processing instruction: {instr}")
        print(f"Arg1: {instr.arg1}")
        print(f"Arg2: {instr.arg2}")
        print(f"Result: {instr.result}")
        print(f"Operation: {instr.op}")

        if instr.op == Operation.PARAM:
            self.handle_param(instr)
            print(f"Current Params: {self.current_params}")
        elif instr.op == Operation.ARG:
            self.current_args.append(instr.arg1)
        elif instr.op == Operation.CALL:
            self.handle_call(instr)
        elif instr.op == Operation.RETURN:
            self.handle_return(instr)
        elif instr.op == Operation.ASSIGN:
            self.handle_assign(instr)
        elif instr.op in {
            Operation.ADD,
            Operation.SUB,
            Operation.MUL,
            Operation.DIV,
            Operation.MOD,
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
        elif instr.op == Operation.PRINT:
            self.handle_print(instr)
        elif instr.op == Operation.PROCEDURE:

            self.procedure_stack.append(instr.result)
            if instr.result not in self.procedures:
                self.procedures[instr.result] = []

            self.add_instruction(f"{instr.result}:")
        elif instr.op == Operation.LABEL:
            self.handle_label(instr)

        elif instr.op == Operation.AND:
            self.handle_and(instr)

        elif instr.op == Operation.OR:
            self.handle_or(instr)

        elif instr.op == Operation.END_PROCEDURE:
            # End of the current procedure
            if len(self.procedure_stack) > 1:
                self.procedure_stack.pop()
            else:
                raise RuntimeError("Cannot end 'main' procedure.")

        else:
            raise ValueError(f"Unsupported operation: {instr.op}")

    def handle_procedure(self, instr: Instruction):
        """
        Handle the start of a procedure.
        """
        self.procedure_stack.append(instr.result)
        if instr.result not in self.procedures:
            self.procedures[instr.result] = []

        self.add_instruction(f"{instr.result}:")

        # Initialize a list to keep track of parameters for this procedure
        self.current_params: List[str] = []

    def handle_param(self, instr: Instruction):
        """
        Assign $a0-$a3 to parameter variables at the start of a procedure.
        """
        param_index = len(self.current_params)
        if param_index >= 4:
            raise ValueError(
                "Procedures with more than 4 parameters are not supported."
            )

        param_reg = f"$a{param_index}"
        param_var = instr.arg1  # Assuming 'PARAM number' where arg1 is 'number'

        # # Ensure the variable is declared
        # self.ensure_variable(param_var)

        # Move from $a register to a temporary register or store directly
        reg = self.get_register(param_var)
        self.add_instruction(f"move {reg}, {param_reg}  # Assign parameter {param_var}")

        # Update descriptors
        self.register_descriptor[reg].add(param_var)
        self.address_descriptor.setdefault(param_var, set()).add(reg)

        self.current_params.append(param_var)

    def handle_and(self, instr: Instruction):
        """
        Handle logical AND operations.
        Translates TAC AND instructions into MIPS instructions.
        """
        reg_result = self.get_register(instr.result)

        # Handle arg1
        if instr.arg1.isdigit():
            const_var1 = f"const_{instr.arg1}"
            temp_reg1 = self.get_register(const_var1)
            self.add_instruction(f"li {temp_reg1}, {instr.arg1}")
            reg_arg1 = temp_reg1
        else:
            reg_arg1 = self.get_register(instr.arg1)
            if instr.arg1 in self.variables:
                self.add_instruction(f"lw {reg_arg1}, {instr.arg1}")

        # Handle arg2
        if instr.arg2.isdigit():
            # Use immediate instruction if possible
            self.add_instruction(
                f"andi {reg_result}, {reg_arg1}, {instr.arg2}  # AND with immediate"
            )
        else:
            reg_arg2 = self.get_register(instr.arg2)
            if instr.arg2 in self.variables:
                self.add_instruction(f"lw {reg_arg2}, {instr.arg2}")
            self.add_instruction(
                f"and {reg_result}, {reg_arg1}, {reg_arg2}  # AND operation"
            )

        # Update register descriptors
        self.register_descriptor[reg_result].add(instr.result)
        self.address_descriptor.setdefault(instr.result, set()).add(reg_result)

        # Free source registers if they were temporary
        if instr.arg1.isdigit():
            self.free_register(f"const_{instr.arg1}")
        if instr.arg2.isdigit():
            self.free_register(f"const_{instr.arg2}")
        else:
            self.free_register(instr.arg2)

    def handle_or(self, instr: Instruction):
        """
        Handle logical OR operations.
        Translates TAC OR instructions into MIPS instructions.
        """
        reg_result = self.get_register(instr.result)

        # Handle arg1
        if instr.arg1.isdigit():
            const_var1 = f"const_{instr.arg1}"
            temp_reg1 = self.get_register(const_var1)
            self.add_instruction(f"li {temp_reg1}, {instr.arg1}")
            reg_arg1 = temp_reg1
        else:
            reg_arg1 = self.get_register(instr.arg1)
            if instr.arg1 in self.variables:
                self.add_instruction(f"lw {reg_arg1}, {instr.arg1}")

        # Handle arg2
        if instr.arg2.isdigit():
            # Use immediate instruction if possible
            self.add_instruction(
                f"ori {reg_result}, {reg_arg1}, {instr.arg2}  # OR with immediate"
            )
        else:
            reg_arg2 = self.get_register(instr.arg2)
            if instr.arg2 in self.variables:
                self.add_instruction(f"lw {reg_arg2}, {instr.arg2}")
            self.add_instruction(
                f"or {reg_result}, {reg_arg1}, {reg_arg2}  # OR operation"
            )

        # Update register descriptors
        self.register_descriptor[reg_result].add(instr.result)
        self.address_descriptor.setdefault(instr.result, set()).add(reg_result)

        # Free source registers if they were temporary
        if instr.arg1.isdigit():
            self.free_register(f"const_{instr.arg1}")
        if instr.arg2.isdigit():
            self.free_register(f"const_{instr.arg2}")
        else:
            self.free_register(instr.arg2)

    def is_register(self, var: str) -> bool:
        return var.startswith("$")

    def ensure_variable(self, var: str):
        """Ensure that a variable is declared in the data section."""
        if var not in self.variables and not self.is_register(var):
            self.variables.add(var)
            self.data_section.append(f"{var}: .word 0")

    def handle_assign(self, instr: Instruction):
        """
        Handle assignment operations by storing variables in .data.
        """

        if instr.arg1.startswith('"'):  # String literal
            label = self.get_string_literal(instr.arg1)
            reg = self.get_register(instr.result)
            self.add_instruction(f"la {reg}, {label}")
            self.add_instruction(f"sw {reg}, {instr.result}")  # Store string address
        elif instr.arg1.isdigit():  # Numeric constant
            self.add_instruction(f"li $t0, {instr.arg1}")  # Load immediate into $t0
            self.add_instruction(f"sw $t0, {instr.result}")  # Store to .data
            self.free_register("const")  # Free the temporary register

            if instr.result not in self.variables:
                self.variables.add(instr.result)
                self.data_section.append(f"{instr.result}: .word 0")
        else:
            if instr.arg1.startswith("t"):

                if instr.result.startswith("t"):
                    reg = self.get_register(instr.result)
                    self.add_instruction(f"move {reg}, {instr.arg1}")
                else:
                    if instr.result not in self.variables:
                        self.variables.add(instr.result)
                        self.data_section.append(f"{instr.result}: .word 0")

                    reg = self.get_register(instr.arg1)
                    self.add_instruction(f"sw {reg}, {instr.result}")

                return

            reg = self.get_register(instr.arg1)

            print(f"Register: {reg}")

            reg_result = self.get_register(instr.result)

            print(f"Result Register: {reg_result}")

    def handle_arithmetic(self, instr: Instruction):
        """
        Handle arithmetic operations: ADD, SUB, MUL, DIV, MOD.
        Translates TAC arithmetic instructions into MIPS instructions.
        """

        # Mapping from Operation to MIPS instruction
        op_map = {
            Operation.ADD: "add",
            Operation.SUB: "sub",
            Operation.MUL: "mul",
            Operation.DIV: "div",
        }

        if instr.op in op_map:
            mips_op = op_map[instr.op]

            # Handle arg1
            if instr.arg1.isdigit():
                const_var1 = f"const_{instr.arg1}"
                # If arg1 is a constant, load it into a temporary register
                temp_reg1 = self.get_register(const_var1)
                self.add_instruction(f"li {temp_reg1}, {instr.arg1}")
                reg_arg1 = temp_reg1
            else:
                reg_arg1 = self.get_register(instr.arg1)

                if instr.arg1 in self.variables:
                    # Load the variable from memory
                    self.add_instruction(f"lw {reg_arg1}, {instr.arg1}")

            # Handle arg2
            if instr.arg2.isdigit():
                const_var2 = f"const_{instr.arg2}"
                # If arg2 is a constant, load it into a temporary register
                temp_reg2 = self.get_register(const_var2)
                self.add_instruction(f"li {temp_reg2}, {instr.arg2}")
                reg_arg2 = temp_reg2
            else:
                # Otherwise, get the register containing arg2
                reg_arg2 = self.get_register(instr.arg2)

                if instr.arg2 in self.variables:
                    # Load the variable from memory
                    self.add_instruction(f"lw {reg_arg2}, {instr.arg2}")

            # Allocate a register for the result
            reg_result = self.get_register(instr.result)

            # Emit the MIPS instruction
            self.add_instruction(f"{mips_op} {reg_result}, {reg_arg1}, {reg_arg2}")
            print("--------------------")
            print(f"{mips_op} {reg_result}, {reg_arg1}, {reg_arg2}")
            print(f"instr.arg1: {instr.arg1}")
            print(f"instr.arg2: {instr.arg2}")
            print("--------------------")

            # Update register descriptors
            self.register_descriptor[reg_result].add(instr.result)
            self.address_descriptor.setdefault(instr.result, set()).add(reg_result)

            # Free the source registers as their values are now in reg_result
            if instr.arg1.isdigit():
                self.free_register(const_var1)  # Free 'const_1'
            else:
                self.free_register(instr.arg1)  # Free variable name

            if instr.arg2.isdigit():
                self.free_register(const_var2)  # Free 'const_2'
            else:
                self.free_register(instr.arg2)  # Free variable name

        elif instr.op == Operation.MOD:
            # For modulo operation, use 'div' and 'mfhi'

            # Handle arg1
            if instr.arg1.isdigit():
                temp_reg1 = self.get_register(f"const_{instr.arg1}")
                self.add_instruction(f"li {temp_reg1}, {instr.arg1}")
                reg_arg1 = temp_reg1
            elif instr.arg1 in self.variables:
                reg_arg1 = self.get_register(instr.arg1)
                self.add_instruction(f"lw {reg_arg1}, {instr.arg1}")
            else:
                reg_arg1 = self.get_register(instr.arg1)

            # Handle arg2
            if instr.arg2.isdigit():
                temp_reg2 = self.get_register(f"const_{instr.arg2}")
                self.add_instruction(f"li {temp_reg2}, {instr.arg2}")
                reg_arg2 = temp_reg2
            elif instr.arg2 in self.variables:
                reg_arg2 = self.get_register(instr.arg2)
                self.add_instruction(f"lw {reg_arg2}, {instr.arg2}")
            else:
                reg_arg2 = self.get_register(instr.arg2)

            # Emit the 'div' instruction
            self.add_instruction(f"div {reg_arg1}, {reg_arg2}")

            reg_result = self.get_register(instr.result)

            # Move the remainder from HI to the result register
            self.add_instruction(f"mfhi {reg_result}")

            if not instr.arg1.startswith("const_"):
                self.free_register(instr.arg1)
            if not instr.arg2.startswith("const_"):
                self.free_register(instr.arg2)

        else:
            raise ValueError(f"Unsupported arithmetic operation: {instr.op}")

        # Update register descriptors
        self.register_descriptor[reg_result].add(instr.result)
        self.address_descriptor.setdefault(instr.result, set()).add(reg_result)

    def handle_comparison(self, instr: Instruction):
        reg_result = self.get_register(instr.result)

        # Handle arg1
        if instr.arg1.isdigit():
            reg_arg1 = self.get_register(instr.arg1)
            self.add_instruction(f"li {reg_arg1}, {instr.arg1}")
        elif instr.arg1 in self.variables:
            reg_arg1 = self.get_register(instr.arg1)
            self.add_instruction(f"lw {reg_arg1}, {instr.arg1}")
        else:
            reg_arg1 = self.get_register(instr.arg1)

        # Handle arg2
        if instr.arg2.isdigit():
            reg_arg2 = self.get_register(instr.arg2)
            self.add_instruction(f"li {reg_arg2}, {instr.arg2}")
        elif instr.arg2 in self.variables:
            reg_arg2 = self.get_register(instr.arg2)
            self.add_instruction(f"lw {reg_arg2}, {instr.arg2}")
        else:
            reg_arg2 = self.get_register(instr.arg2)

        print(f"Comparing {instr.arg1} and {instr.arg2}")

        op_map = {
            Operation.GT: "sgt",
            Operation.LT: "slt",
            Operation.GE: "sge",
            Operation.LE: "sle",
            Operation.EQ: "seq",
            Operation.NE: "sne",
        }

        self.add_instruction(
            f"{op_map[instr.op]} {reg_result}, {reg_arg1}, {reg_arg2} # {instr.op}"
        )

        # Update register descriptors
        self.register_descriptor[reg_result].add(instr.result)
        self.address_descriptor.setdefault(instr.result, set()).add(reg_result)

        # Free source registers after use
        self.free_register(instr.arg1)
        self.free_register(instr.arg2)

    def handle_if_false(self, instr: Instruction):
        reg = self.get_register(instr.arg1)
        self.add_instruction(f"beq {reg}, $zero, {instr.result}")

    def handle_goto(self, instr: Instruction):
        self.add_instruction(f"j {instr.result}  # goto {instr.result}")

    def handle_call(self, instr: Instruction):
        """
        Handle procedure call by moving arguments to $a0-$a3 and issuing 'jal'.
        """
        arg_registers = ["$a0", "$a1", "$a2", "$a3"]
        num_args = len(self.current_args)

        if num_args > 4:
            raise ValueError(
                "Function calls with more than 4 parameters are not supported."
            )

        # Move each argument to the corresponding $a register
        for i in range(num_args):
            arg = self.current_args[i]
            reg = arg_registers[i]
            if arg.isdigit():
                self.add_instruction(f"li {reg}, {arg}  # Load immediate argument")
            else:
                arg_reg = self.get_register(arg)
                self.add_instruction(f"lw {reg}, {arg}  # Load argument from {arg}")
                self.free_register(arg)

        # Clear the current_args list after moving arguments
        self.current_args = []

        # Jump and link to the procedure
        self.add_instruction(f"jal {instr.arg1}  # Call procedure {instr.arg1}")

    def handle_return(self, instr: Instruction):
        """
        Handle procedure return operations by emitting 'jr $ra'.
        """
        self.add_instruction("jr $ra  # Return from procedure")

    def handle_label(self, instr: Instruction):
        self.add_instruction(f"{instr.result}:")

    def handle_print(self, instr: Instruction):
        """
        Handle print operations by determining the type of the argument
        and emitting the appropriate syscall.
        """
        var = instr.arg1

        if var.startswith('"') and var.endswith('"'):  # String literal
            label = self.get_string_literal(var)
            self.add_instruction("li $v0, 4  # Print string syscall")
            self.add_instruction(f"la $a0, {label}  # Load address of string to print")
            self.add_instruction("syscall")
        else:
            # Assume it's an integer variable
            reg = self.get_register(var)
            if var in self.variables:
                self.add_instruction(f"lw {reg}, {var}  # Load integer to print")
            self.add_instruction("li $v0, 1  # Print integer syscall")
            self.add_instruction(f"move $a0, {reg}  # Move integer to $a0")
            self.add_instruction("syscall")

            # Free the register if it's a temporary
            if var.startswith("const_"):
                self.free_register(var)
            else:
                self.free_register(var)

    def get_string_literal(self, value: str) -> str:
        """Ensure a string literal is in the data section."""
        if value not in self.string_literals:
            label = f"str_{len(self.string_literals)}"

            self.string_literals[value] = label
            self.data_section.append(f"{label}: .asciiz {value}")
        return self.string_literals[value]

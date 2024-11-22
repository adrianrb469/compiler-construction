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
        """
        Allocate a register for a variable.
        If the variable is in memory, load it into a register.
        """

        # If the variable is already in a register, return the register
        for reg, vars in self.register_descriptor.items():
            if var in vars:
                return reg

        # If the variable is in memory, load it into a register
        if var in self.address_descriptor:
            memory_locations = self.address_descriptor[var]
            for addr in memory_locations:
                if "($sp)" in addr:  # Check if the variable is in stack memory
                    print(f"Loading {var} from memory")

                    # Allocate a free register
                    for reg, vars in self.register_descriptor.items():
                        if not vars:
                            # Load from memory into the register
                            self.add_instruction(
                                f"lw {reg}, {addr}  # Load {var} from memory"
                            )
                            self.register_descriptor[reg].add(var)
                            self.address_descriptor[var].add(reg)
                            return reg

        # If the variable is not in memory or a register, allocate an empty register
        for reg, vars in self.register_descriptor.items():
            if not vars:
                self.register_descriptor[reg].add(var)
                self.address_descriptor.setdefault(var, set()).add(reg)
                return reg

        # If all registers are full, spill one to memory
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
        """
        Get the stack offset for a variable, assuming it has been pushed to the stack.
        """
        if var in self.address_descriptor and any(
            "($sp)" in addr for addr in self.address_descriptor[var]
        ):
            # Return the existing offset for the variable
            for addr in self.address_descriptor[var]:
                if "($sp)" in addr:
                    return addr
        else:
            # Allocate new space for the variable
            self.stack_offset += 4
            self.address_descriptor[var] = {f"-{self.stack_offset}($sp)"}
            return f"-{self.stack_offset}($sp)"

    def add_instruction(self, instruction: str, start_of_procedure: bool = False):
        """
        Append an instruction to the current procedure.
        """

        current_procedure = self.procedure_stack[-1]

        if start_of_procedure:
            # @Hack: to allocate space for $ra at the start of a procedure
            print("Allocating space for $ra, at ", current_procedure)
            print(self.procedures[current_procedure])
            self.procedures[current_procedure].insert(1, instruction)
        else:
            self.procedures[current_procedure].append(instruction)

    def generate(self, instructions: List[Instruction]) -> str:
        """
        Modified generate method to include class vtable setup.
        """
        # Start with original data and text sections
        self.data_section = [".data"]
        self.text_section = [".text", "main:"]

        # Process all instructions
        for instr in instructions:
            self.process_instruction(instr)

        # Add exit syscall
        self.add_instruction("li $v0, 10")
        self.add_instruction("syscall")

        # Combine sections with proper formatting
        indented_data_section = [self.data_section[0]]
        for line in self.data_section[1:]:
            indented_data_section.append(f"    {line}")

        text_section = [".text"]
        for proc_name in ["main"] + [p for p in self.procedures if p != "main"]:
            if proc_name != "main":
                text_section.append("")
            text_section.append(f"{proc_name}:")

            for line in self.procedures[proc_name]:
                if line.endswith(":") or line.startswith("."):
                    text_section.append(line)
                else:
                    text_section.append(f"    {line}")

        final_code = "\n".join(indented_data_section + text_section)
        return final_code

    def process_instruction(self, instr: Instruction):

        if instr.op == Operation.PARAM:
            self.handle_param(instr)
        elif instr.op == Operation.ARG:
            self.current_args.append(instr.arg1)
        elif instr.op == Operation.CALL:
            self.handle_call(instr)
        elif instr.op == Operation.RETURN:
            self.handle_return(instr)
        elif instr.op == Operation.ASSIGN:
            self.handle_assign(instr)
        elif instr.op == Operation.ALLOCATE:  # Add ALLOCATE handling
            self.handle_allocate(instr)
        elif instr.op == Operation.STORE_FIELD:  # Add STORE_FIELD handling
            self.handle_store_field(instr)
        elif instr.op == Operation.LOAD_METHOD:  # Add LOAD_METHOD handling
            self.handle_load_method(instr)
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
            self.handle_procedure(instr)
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
            print(f"{instr.op} is not a valid instruction.")
            # raise ValueError(f"Unsupported operation: {instr.op}")

    def handle_procedure(self, instr: Instruction):
        """
        Handle the start of a procedure.
        """
        procedure_name = instr.result
        self.procedure_stack.append(procedure_name)

        if procedure_name not in self.procedures:
            self.procedures[instr.result] = []

        self.add_instruction(f"{instr.result}:")

        # self.add_instruction("addi $sp, $sp, -4  # Allocate space for $ra")
        self.add_instruction("sw $ra, 0($sp)    # Save return address")

        self.current_params: List[str] = []

        self.stack_offset = 4

    def handle_param(self, instr: Instruction):
        """
        Allocate stack space and assign $a0-$a3 to parameter variables at the start of a procedure.
        Handles all parameters at once.
        """
        # Split parameters and append them into stack/registers

        args = instr.arg1.split(",")  # Split the comma-separated parameters

        if len(args) > 4:
            raise ValueError(
                "Procedures with more than 4 parameters are not supported."
            )

        # Allocate stack space for all parameters
        total_size = len(args) * 4 + 4  # 4 bytes for each parameter + 4 bytes for $ra

        self.add_instruction(
            f"addi $sp, $sp, -{total_size}", start_of_procedure=True
        )  # Allocate stack space

        self.stack_offset += total_size  # Update total stack offset

        # Assign parameters to registers and stack
        for i, param_var in enumerate(args):
            param_reg = f"$a{i}"  # Argument register ($a0-$a3)
            s_reg = f"$s{i}"  # Temporary storage register ($s0-$s3)

            # Move from argument register to temporary register
            self.add_instruction(f"move {s_reg}, {param_reg}")

            # Calculate stack offset for this parameter
            offset = (i + 1) * 4
            self.add_instruction(f"sw {s_reg}, -{offset}($sp)")

            # Update address descriptor for the variable
            self.address_descriptor[param_var] = {f"-{offset}($sp)"}

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
        Enhanced assign handler with object support
        """
        print("Handling assignment:", instr)

        if instr.arg1.startswith('t'):  # Temporary variable assignment
            source_reg = self.get_register(instr.arg1)
            if instr.result not in self.variables:
                self.variables.add(instr.result)
                self.data_section.append(f"{instr.result}: .word 0")
            self.add_instruction(f"sw {source_reg}, {instr.result}")
        else:
            # Original assign handling
            if instr.arg1.startswith('"'):  # String literal
                label = self.get_string_literal(instr.arg1)
                reg = self.get_register(instr.result)
                self.add_instruction(f"la {reg}, {label}")
                self.add_instruction(f"sw {reg}, {instr.result}")
            elif instr.arg1.isdigit():  # Numeric constant
                if instr.result not in self.variables:
                    self.variables.add(instr.result)
                    self.data_section.append(f"{instr.result}: .word 0")
                self.add_instruction(f"li $t0, {instr.arg1}")
                self.add_instruction(f"sw $t0, {instr.result}")
            else:
                reg = self.get_register(instr.arg1)
                reg_result = self.get_register(instr.result)
                self.add_instruction(f"move {reg_result}, {reg}")

    def log_tac(self, instr: Instruction) -> str:
        parts = [f"Operation: {instr.op}"]
        if instr.arg1 is not None:
            parts.append("Arg1: " + instr.arg1)
        if instr.arg2 is not None:
            parts.append("Arg2: " + instr.arg2)
        if instr.result is not None:
            parts.append("Result: " + instr.result)

        formatted_tac = " ".join(parts)
        print(formatted_tac)
        return formatted_tac

    def handle_arithmetic(self, instr: Instruction):
        """
        Handle arithmetic operations: ADD, SUB, MUL, DIV, MOD.
        Translates TAC arithmetic instructions into MIPS instructions.
        """

        self.log_tac(instr)

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
        Handle procedure calls, including method calls.
        """
        # Save return address
        self.add_instruction("subu $sp, $sp, 4")
        self.add_instruction("sw $ra, 0($sp)")

        # Move arguments to argument registers
        arg_registers = ["$a0", "$a1", "$a2", "$a3"]
        num_args = len(self.current_args)

        if num_args > 4:
            raise ValueError("Function calls with more than 4 parameters are not supported.")

        # Move each argument to the corresponding $a register
        for i in range(num_args):
            arg = self.current_args[i]
            reg = arg_registers[i]
            if arg.isdigit():
                self.add_instruction(f"li {reg}, {arg}")
            elif arg.startswith('"'):
                label = self.get_string_literal(arg)
                self.add_instruction(f"la {reg}, {label}")
            else:
                arg_reg = self.get_register(arg)
                self.add_instruction(f"move {reg}, {arg_reg}")

        # Clear the current_args list
        self.current_args = []

        # Handle different types of calls
        if isinstance(instr.arg1, str) and instr.arg1.startswith("t"):
            # Method call through temporary
            method_reg = self.get_register(instr.arg1)
            self.add_instruction(f"jalr {method_reg}")
        else:
            # Direct procedure call
            self.add_instruction(f"jal {instr.arg1}")

        # Restore return address
        self.add_instruction("lw $ra, 0($sp)")
        self.add_instruction("addu $sp, $sp, 4")

        # Store result if needed
        if instr.result:
            result_reg = self.get_register(instr.result)
            self.add_instruction(f"move {result_reg}, $v0")

    def handle_return(self, instr: Instruction):
        """
        Handle procedure return operations by setting the return value,
        restoring $ra, cleaning up the stack, and emitting 'jr $ra'.
        """
        if instr.arg1:  # If there is a value to return
            # Load the return value into $v0
            reg = self.get_register(
                instr.arg1
            )  # Get the register holding the return value
            self.add_instruction(f"move $v0, {reg}  # Set return value into $v0")

        # Restore $ra from the stack
        self.add_instruction("lw $ra, 0($sp)  # Restore return address")

        # Clean up stack space for parameters and local variables
        self.add_instruction(f"addi $sp, $sp, {self.stack_offset}  # Clean up stack")

        # Return to the caller
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

        # Remove the existing quotes
        value = value[1:-1]

        if value not in self.string_literals:
            label = f"str_{len(self.string_literals)}"
            self.string_literals[value] = label

            # Re-add quotes around the value and include the newline
            self.data_section.append(f'{label}: .asciiz "{value}\\n"\n')
        return self.string_literals[value]

    def handle_allocate(self, instr: Instruction):
        """
        Handle object allocation and vtable setup
        """
        # Add class vtable to data section
        class_name = instr.arg1
        vtable_label = f"{class_name}_vtable"
        if vtable_label not in self.variables:
            self.variables.add(vtable_label)
            self.data_section.append(f"{vtable_label}: .word {class_name}.init, {class_name}.saludar")

        # Allocate memory for object
        self.add_instruction("li $v0, 9")  # sbrk syscall
        self.add_instruction("li $a0, 32")  # Allocate 32 bytes for object
        self.add_instruction("syscall")

        # Get result register and store object address
        reg_result = self.get_register(instr.result)
        self.add_instruction(f"move {reg_result}, $v0")

        # Set up vtable pointer
        self.add_instruction(f"la $t0, {vtable_label}")
        self.add_instruction(f"sw $t0, 0({reg_result})")

    def handle_store_field(self, instr: Instruction):
        """
        Handle storing fields in objects
        """
        # Get object register ('this' pointer)
        obj_reg = self.get_register(instr.result)

        # Get value register
        if instr.arg1 in self.variables:
            value_reg = self.get_register(instr.arg1)
            self.add_instruction(f"lw {value_reg}, {instr.arg1}")
        else:
            value_reg = self.get_register(instr.arg1)

        # Calculate field offset
        field_offsets = {
            "nombre": 4,
            "apellido": 8
        }
        offset = field_offsets.get(instr.arg2, 4)  # Default to 4 if field not found

        # Store the field
        self.add_instruction(f"sw {value_reg}, {offset}({obj_reg})")

    def handle_load_method(self, instr: Instruction):
        """
        Handle loading method addresses from vtable
        """
        # Get object register
        obj_reg = self.get_register(instr.arg1)

        # Get vtable address
        temp_reg = self.get_register("temp")
        self.add_instruction(f"lw {temp_reg}, 0({obj_reg})")

        # Calculate method offset
        method_offsets = {
            "init": 0,
            "saludar": 4
        }
        offset = method_offsets.get(instr.arg2, 0)

        # Load method address
        result_reg = self.get_register(instr.result)
        self.add_instruction(f"lw {result_reg}, {offset}({temp_reg})")

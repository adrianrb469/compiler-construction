from .semantic_analyzer import analyze
from .tac_generator import generate_tac
from .mips_generator import MIPSCodeGenerator


def compile(code: str):
    _, errors, table, table_obj = analyze(code)

    if len(errors) == 0:
        print("Generating TAC")
        formatted_tac, tac = generate_tac(code, table_obj)
        assembly_code = MIPSCodeGenerator().generate(tac)

        return formatted_tac, table, None, table_obj, assembly_code
    else:
        return None, None, errors, None, None

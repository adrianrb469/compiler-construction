from .semantic_analyzer import analyze
from .tac_generator import generate_tac


def compile(code: str):
    tree, errors, table, table_obj = analyze(code)

    if len(errors) == 0:
        print("Generating TAC")
        three_address_code = generate_tac(code, table_obj)

        return three_address_code, table, None, table_obj
    else:
        return None, None, errors, None

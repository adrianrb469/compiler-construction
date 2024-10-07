from .semantic_analyzer import analyze
from .tac_generator import generate_tac


def compile(code: str):
    tree, errors, table = analyze(code)

    if len(errors) == 0:
        three_address_code = generate_tac(code)

        return three_address_code, table, None
    else:
        return None, None, errors

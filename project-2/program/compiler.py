from .Driver import analyzer
from .semantic_analyzer import compile_code

def compiler(code: str):
  tree, errors, table = analyzer(code)
  if len(errors) == 0:
    compiled_code = compile_code(code)
    return compiled_code, table, None
  else:
    return None, None, errors

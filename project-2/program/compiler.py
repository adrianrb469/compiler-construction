from .Driver import analyzer

def compiler(code: str):
  tree, errors, table = analyzer(code)
  if len(errors) == 0:
    compiled_code = code
    return compiled_code, table, None
  else:
    return "", {}, errors

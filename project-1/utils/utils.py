def getDeclType (type: str) -> str:
    if type == "INT":
        return f"Int"
    elif type == "STRING":
        return f"String"
    elif type == "BOOLEAN":
        return f"Boolean"
    elif type == "FLOAT":
        return f"Float"
    else:
        return type

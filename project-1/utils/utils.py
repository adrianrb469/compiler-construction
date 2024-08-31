from typing import Optional
from program.SymbolTable import DataType


def getDeclType(type: str) -> str:
    if type == "INT":
        return "Int"
    elif type == "STRING":
        return "String"
    elif type == "BOOLEAN":
        return "Boolean"
    elif type == "FLOAT":
        return "Float"
    else:
        return type


def types_comparable(typeA: DataType, typeB: DataType) -> bool:
    if typeA == typeB:
        return True
    if (typeA == DataType.FLOAT and typeB == DataType.INT) or (
        typeA == DataType.INT and typeB == DataType.FLOAT
    ):
        return True
    if DataType.ANY in [typeA, typeB]:
        # ? Should this be false?
        return True
    if typeA == DataType.NULL or typeB == DataType.NULL:
        return True
    return False


def arithmetic_op(left: DataType, op: str, right: DataType) -> Optional[DataType]:
    if left in [DataType.INT, DataType.FLOAT] and right in [
        DataType.INT,
        DataType.FLOAT,
    ]:
        if op in ["+", "-", "*"]:
            return DataType.FLOAT if DataType.FLOAT in [left, right] else DataType.INT
        elif op == "/":
            return DataType.FLOAT
        elif op == "%":
            if left == DataType.INT and right == DataType.INT:
                return DataType.INT
    return None

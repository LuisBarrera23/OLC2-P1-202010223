from enum import IntEnum

class TipoDato(IntEnum):
    I64 = 0,
    F64 = 1,
    BOOL = 2,
    CHAR = 3,
    STRING = 4,
    STR = 5,
    USIZE = 6,
    ARREGLO = 7,
    ERROR = 8,

class RetornoType:
    def __init__(self, valor=None, tipo=TipoDato.ERROR):
        self.valor=valor
        self.tipo=tipo
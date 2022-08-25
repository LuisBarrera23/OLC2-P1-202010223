from enum import Enum
from src.Abstract.RetornoType import RetornoType

from src.Abstract.Expresion import Expresion

class Primitivo(Expresion):

    def __init__(self,valor,tipo):
        self.valor=valor
        self.tipo=tipo

    def obtenerValor(self,entorno):
        return RetornoType(self.valor , self.tipo)
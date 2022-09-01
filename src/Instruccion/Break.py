from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import RetornoType

class Break(Instruccion):

    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
        self.Retorno=RetornoType()

    def Ejecutar(self, entorno):
        if self.expresion!=None:
            self.Retorno=self.expresion.obtenerValor(entorno)
        return self

from src.Abstract.Instruccion import Instruccion


class Print(Instruccion):
    pass

    def __init__(self,expresion):
        self.expresion=expresion
        self.linea = 0
        self.columna = 0

    def Ejecutar(self, entorno):
        pass

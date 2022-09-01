from src.Abstract.Instruccion import Instruccion

class Continue(Instruccion):
    def __init__(self, linea, columna):
        self.linea=linea
        self.columna=columna

    def Ejecutar(self, entorno):
        return self
from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import TipoDato

from src.Symbol.ArrayInstancia import ArrayInstancia

from src.Symbol.Error import Error
from src.PatronSingleton.Singleton import Singleton


class DeclaracionVector(Instruccion):

    def __init__(self,idInstancia, expresion, linea, columna,dimensiones=None,mutable=False):
        self.idInstancia = idInstancia
        self.dimensiones = dimensiones
        self.expresion = expresion
        self.linea=linea
        self.columna=columna
        self.mutable=mutable

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        
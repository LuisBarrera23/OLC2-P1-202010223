from src.Abstract.RetornoType import RetornoType

from src.Abstract.Expresion import Expresion

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Symbol.ArrayInstancia import ArrayInstancia

class AccesoSimbolo(Expresion):

    def __init__(self,id,linea,columna):
        self.id=id
        self.linea=linea
        self.columna=columna

    def obtenerValor(self,entorno):
        s=Singleton.getInstance()
        if entorno.existeSimbolo(self.id):
            E=entorno.obtenerSimbolo(self.id)
            if isinstance(E,ArrayInstancia):
                return RetornoType(valor=E,tipo=E.tipo)
            return RetornoType(valor=E.valor,tipo=E.tipo)
        else:
            raise Exception(s.addError(Error(f"Variable {self.id} no existe",self.linea,self.columna)))

from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato
from src.Symbol.ArrayInstancia import ArrayInstancia

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class Referencia(Expresion):
    def __init__(self, idArreglo, linea, columna):
        self.idArreglo = idArreglo
        self.linea=linea
        self.columna=columna

    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        if entorno.existeSimbolo(self.idArreglo) is not True:
            raise Exception(s.addError(Error(f"Arreglo {self.id} no existe",self.linea,self.columna)))

        arreglo = entorno.obtenerSimbolo(self.idArreglo)
        # print(arreglo)
        # if isinstance(arreglo, ArrayInstancia) is not True:
        #     raise Exception(s.addError(Error(f"No es referencia de un arreglo",self.linea,self.columna)))

        return RetornoType(valor = self.idArreglo, tipo=arreglo.tipo)
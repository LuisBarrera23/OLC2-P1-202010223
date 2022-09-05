
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import TipoDato,RetornoType

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Expresion.AccesoSimbolo import AccesoSimbolo
from src.Expresion.AccesoSimbolo import ArrayInstancia
from src.Expresion.AccesoArreglo import AccesoArreglo


class Len(Expresion):
    def __init__(self,expresion,linea,columna) -> None:
        self.expresion:Expresion=expresion
        self.linea=linea
        self.columna=columna
        
    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        retorno=RetornoType(valor=None,tipo=TipoDato.ERROR)

        if isinstance(self.expresion,AccesoSimbolo):
            if entorno.existeSimbolo(self.expresion.id)==False:
                raise Exception(s.addError(Error(f"No existe arreglo con este ID",self.linea,self.columna)))
            arreglo=entorno.obtenerSimbolo(self.expresion.id)
            if isinstance(arreglo,ArrayInstancia):
                #print(arreglo.tipo)
                return RetornoType(valor=len(arreglo.valores),tipo=TipoDato.I64)
            else:
                raise Exception(s.addError(Error(f"Esta expresion no puede ser operada con len()",self.linea,self.columna)))
        elif isinstance(self.expresion,AccesoArreglo):
            #print(self.expresion)
            E=self.expresion.obtenerValor(entorno)
            #print(len(E.valor))
            return RetornoType(valor=len(E.valor),tipo=TipoDato.I64)
        return retorno
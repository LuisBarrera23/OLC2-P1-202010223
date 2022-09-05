
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import TipoDato,RetornoType

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Expresion.AccesoSimbolo import AccesoSimbolo
from src.Expresion.AccesoSimbolo import ArrayInstancia
from src.Expresion.AccesoArreglo import AccesoArreglo

from src.Symbol.Symbol import Simbolo


class Remove(Expresion):
    def __init__(self,expresion,expresion2,linea,columna) -> None:
        self.expresion:Expresion=expresion
        self.expresion2=expresion2
        self.linea=linea
        self.columna=columna
        
    def obtenerValor(self, entorno):
        s=Singleton.getInstance()

        if isinstance(self.expresion,AccesoSimbolo):
            if entorno.existeSimbolo(self.expresion.id)==False:
                raise Exception(s.addError(Error(f"No existe arreglo con este ID",self.linea,self.columna)))
            arreglo=entorno.obtenerSimbolo(self.expresion.id)
            #print(arreglo)
            if isinstance(arreglo,ArrayInstancia):
                #print(arreglo.tipo)
                raise Exception(s.addError(Error(f"remove es solo para vectores",self.linea,self.columna)))
            if isinstance(arreglo,Simbolo):
                E=self.expresion2.obtenerValor(entorno)
                print(arreglo.valor)
                elemento=arreglo.valor.pop(E.valor)
                return RetornoType(valor=elemento,tipo=arreglo.tipo)
            else:
                raise Exception(s.addError(Error(f"Esta expresion no puede ser operada con remove()",self.linea,self.columna)))
        elif isinstance(self.expresion,AccesoArreglo):
            raise Exception(s.addError(Error(f"remove es solo para vectores",self.linea,self.columna)))
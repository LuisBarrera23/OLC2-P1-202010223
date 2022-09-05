
from src.Abstract.Instruccion import Instruccion
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import TipoDato,RetornoType

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Expresion.AccesoSimbolo import AccesoSimbolo
from src.Expresion.AccesoSimbolo import ArrayInstancia
from src.Expresion.AccesoArreglo import AccesoArreglo

from src.Symbol.Symbol import Simbolo


class Push(Instruccion):
    def __init__(self,id,expresion2,linea,columna) -> None:
        self.id=id
        self.expresion2=expresion2
        self.linea=linea
        self.columna=columna
        
    def Ejecutar(self, entorno):
        s=Singleton.getInstance()

        if entorno.existeSimbolo(self.id)==False:
            raise Exception(s.addError(Error(f"Vector no existe",self.linea,self.columna)))

        vector=entorno.obtenerSimbolo(self.id)
        if isinstance(vector,Simbolo):
            E=self.expresion2.obtenerValor(entorno)
            print(vector.valor)
            vector.valor.append(E.valor)
            return
        elif isinstance(self.expresion,AccesoArreglo):
            raise Exception(s.addError(Error(f"push es solo para vectores",self.linea,self.columna)))
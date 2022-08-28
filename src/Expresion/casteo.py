from lib2to3.pgen2.token import STRING
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import TipoDato,RetornoType

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class Casteo(Expresion):
    def __init__(self,expresion,linea,columna,tipo=None) -> None:
        self.expresion:Expresion=expresion
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        
    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        retorno=RetornoType(valor=None,tipo=TipoDato.ERROR)
        E1=self.expresion.obtenerValor(entorno)
        if(self.tipo==None):
            if(E1.tipo==TipoDato.STR or E1.tipo==TipoDato.STRING):
                return RetornoType(valor=E1.valor,tipo=TipoDato.STRING)
            else:
                raise Exception(s.addError(Error(f"Se necesita un cadena para ejecutar to_string o to_owned",self.linea,self.columna)))
        else:
            if(E1.tipo==TipoDato.I64 or E1.tipo==TipoDato.F64):
                if(self.tipo==TipoDato.I64):
                    retorno.valor=int(E1.valor)
                    retorno.tipo=TipoDato.I64
                    return retorno
                elif(self.tipo==TipoDato.F64):
                    retorno.valor=float(E1.valor)
                    retorno.tipo=TipoDato.F64
                    return retorno
        return retorno
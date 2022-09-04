from cmath import sqrt
import imp
from lib2to3.pgen2.token import STRING
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import TipoDato,RetornoType

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error


class Nativa(Expresion):
    def __init__(self,expresion,tipo,linea,columna) -> None:
        self.expresion:Expresion=expresion
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        
    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        retorno=RetornoType(valor=None,tipo=TipoDato.ERROR)
        E1=self.expresion.obtenerValor(entorno)
        #raise Exception(s.addError(Error(f"Se necesita un cadena para ejecutar to_string o to_owned",self.linea,self.columna)))
        if(self.tipo==1):
            if E1.tipo==TipoDato.I64 or E1.tipo==TipoDato.F64:
                return RetornoType(valor=int(abs(E1.valor)),tipo=TipoDato.I64)
            else:
                raise Exception(s.addError(Error(f"Se necesita tipo de dato I64 o F64 para la funcion abs()",self.linea,self.columna)))
        elif self.tipo==2:
            if E1.tipo==TipoDato.I64 or E1.tipo==TipoDato.F64:
                return RetornoType(valor=int(pow(E1.valor,0.5)),tipo=TipoDato.I64)
            else:
                raise Exception(s.addError(Error(f"Se necesita tipo de dato I64 o F64 para la funcion sqrt()",self.linea,self.columna)))
        return retorno
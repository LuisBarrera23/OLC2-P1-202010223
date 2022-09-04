from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class Dimension(Expresion):
    def __init__(self,dimensiones, tipo, linea, columna):
        self.dimensiones=dimensiones
        self.tipo=tipo
        self.linea=linea
        self.columna=columna

    def obtenerValor(self, entorno) -> RetornoType:
        val=[]
        s=Singleton.getInstance()
        for d in self.dimensiones:
            temp=d.obtenerValor(entorno)
            if temp.tipo==TipoDato.I64:
                val.append(int(temp.valor))
            else:
                raise Exception(s.addError(Error(f"se necesitan valores de tipo enteros para definir dimensiones del array",self.linea,self.columna)))
            
        return RetornoType(valor=val,tipo=self.tipo)
from src.Abstract.RetornoType import TipoDato
from src.Abstract.Instruccion import Instruccion
from src.Symbol.Symbol import Simbolo
from src.Symbol.EntornoTabla import EntornoTabla
from src.Instruccion.Return import Return
from src.Instruccion.Break import Break
from src.Instruccion.Continue import Continue

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class If_i(Instruccion):
    def __init__(self, condicion, verdadero, falso,linea, columna):
        self.condicion=condicion
        self.verdadero=verdadero
        self.falso=falso
        self.linea=linea
        self.columna=columna
        
    def Ejecutar(self, entorno):
        nuevo_entorno=EntornoTabla(entorno)
        E=self.condicion.obtenerValor(entorno)
        s=Singleton.getInstance()
        if E.tipo != TipoDato.BOOL:
            raise Exception(s.addError(Error(f"Instruccion if necesita una expresion booleana",self.linea,self.columna)))
        if E.valor==True:
            for instruccion in self.verdadero:
                retorno=instruccion.Ejecutar(nuevo_entorno)
                if isinstance(retorno,Return):
                    return retorno
                elif isinstance(retorno,Break):
                    return retorno
                elif isinstance(retorno,Continue):
                        return retorno

        else:
            if isinstance(self.falso, If_i):
                return self.falso.Ejecutar(nuevo_entorno)
            else:
                for instruccion in self.falso:
                    retorno=instruccion.Ejecutar(nuevo_entorno)
                    if isinstance(retorno,Return):
                        return retorno
                    elif isinstance(retorno,Break):
                        return retorno
                    elif isinstance(retorno,Continue):
                        return retorno
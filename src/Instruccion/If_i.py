from src.Abstract.RetornoType import TipoDato
from src.Abstract.Instruccion import Instruccion
from src.Symbol.Symbol import Simbolo
from src.Symbol.EntornoTabla import EntornoTabla

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
        E=self.condicion.obtenerValor(entorno)
        s=Singleton.getInstance()
        if E.tipo != TipoDato.BOOL:
            raise Exception(s.addError(Error(f"Instruccion if necesita una expresion booleana",self.linea,self.columna)))

        if E.valor:
            nuevo_entorno=EntornoTabla(entorno)
            for instruccion in self.verdadero:
                instruccion.Ejecutar(nuevo_entorno)

        else:
            if isinstance(self.falso, If_i):
                self.falso.Ejecutar(entorno)
            else:
                nuevo_entorno=EntornoTabla(entorno)
                for instruccion in self.falso:
                    instruccion.Ejecutar(nuevo_entorno)
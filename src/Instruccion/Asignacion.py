from src.Abstract.RetornoType import TipoDato
from src.Abstract.Instruccion import Instruccion
from src.Symbol.Symbol import Simbolo

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class Asignacion(Instruccion):
    def __init__(self, id, expresion,linea,columna):
        self.id=id
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
        
    def Ejecutar(self, entorno):
        E=self.expresion.obtenerValor(entorno)
        existe=entorno.existeSimbolo(self.id)
        s=Singleton.getInstance()
        if existe is False:
            raise Exception(s.addError(Error(f"Variable {self.id} no existe",self.linea,self.columna)))
        else:
            exp=entorno.obtenerSimbolo(self.id)
            #print(E.tipo,exp.tipo)
            if exp.editable is False:
                raise Exception(s.addError(Error(f"Variable {self.id} no es mutable",self.linea,self.columna)))
            if E.tipo==TipoDato.I64 and exp.tipo==TipoDato.USIZE:
                entorno.modificarSimbolo(self.id,E.valor)
            elif E.tipo==exp.tipo:
                entorno.modificarSimbolo(self.id,E.valor)
            else:
                raise Exception(s.addError(Error(f"Variable {self.id} no es del mismo tipo de dato que la expresion",self.linea,self.columna)))

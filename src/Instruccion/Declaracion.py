from src.Abstract.RetornoType import TipoDato
from src.Abstract.Instruccion import Instruccion
from src.Symbol.Symbol import Simbolo

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class Declaracion(Instruccion):
    def __init__(self, id, expresion, mutable,linea,columna, tipo=None):
        self.id=id
        self.expresion=expresion
        self.mutable=mutable
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        
    def Ejecutar(self, entorno):
        E=self.expresion.obtenerValor(entorno)
        existe=entorno.existeSimboloEnEntornoActual(self.id)
        s=Singleton.getInstance()
        if existe:
            raise Exception(s.addError(Error(f"Variable {self.id} ya existente en este entorno",self.linea,self.columna)))
        if self.tipo==None:
            nueva=Simbolo()
            nueva.Simbolo_primitivo(self.id,E.valor,E.tipo,self.linea,self.columna,self.mutable)
            entorno.agregarSimbolo(nueva)
        else:
            if E.tipo==TipoDato.I64 and self.tipo==TipoDato.USIZE:
                nueva=Simbolo()
                nueva.Simbolo_primitivo(self.id,E.valor,self.tipo,self.linea,self.columna,self.mutable)
                #print(nueva.tipo)
                entorno.agregarSimbolo(nueva)
            elif E.tipo==self.tipo:
                nueva=Simbolo()
                nueva.Simbolo_primitivo(self.id,E.valor,E.tipo,self.linea,self.columna,self.mutable)
                #print(nueva.tipo)
                entorno.agregarSimbolo(nueva)
            else:
                raise Exception(s.addError(Error("Tipo de expresion no coincide con el tipo de dato especificado",self.linea,self.columna)))
from hashlib import new
from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import TipoDato

from src.Symbol.ArrayInstancia import ArrayInstancia

from src.Symbol.Error import Error
from src.PatronSingleton.Singleton import Singleton

from src.Symbol.Symbol import Simbolo


class DeclaracionVector(Instruccion):

    def __init__(self,idInstancia, expresion, linea, columna,dimensiones=None,mutable=False,tipo=None,nuevo=False):
        self.idInstancia = idInstancia
        self.dimensiones = dimensiones
        self.expresion = expresion
        self.linea=linea
        self.columna=columna
        self.mutable=mutable
        self.tipo=tipo
        self.nuevo=nuevo
        self.cap=False


    def Ejecutar(self, entorno):
        s=Singleton.getInstance()

        if entorno.existeSimbolo(self.idInstancia):
            raise Exception(s.addError(Error(f"Variable ya existente con el nombre {self.idInstancia}",self.linea,self.columna)))
        
        if self.cap:
            E=self.expresion.expresiones.obtenerValor(entorno)
            nuevo=Simbolo()
            nuevo.Simbolo_vector(self.idInstancia,0,[],E.valor,self.tipo,self.mutable)
            #print(nuevo.capacidad)
            entorno.agregarSimbolo(nuevo)
            return
        E=self.expresion.obtenerValor(entorno)
        #print(E.valor,E.tipo)
        if self.nuevo:
            nuevo=Simbolo()
            nuevo.Simbolo_vector(self.idInstancia,len(E.valor),E.valor,self.expresion.capacidad,self.tipo,self.mutable)
            entorno.agregarSimbolo(nuevo)
            return
        

        if self.tipo!=None:
            if self.tipo!=E.tipo:
                raise Exception(s.addError(Error(f"Vector con tipos diferentes",self.linea,self.columna)))

        nuevo=Simbolo()
        nuevo.Simbolo_vector(self.idInstancia,len(E.valor),E.valor,self.expresion.capacidad,self.mutable)
        
        entorno.agregarSimbolo(nuevo)

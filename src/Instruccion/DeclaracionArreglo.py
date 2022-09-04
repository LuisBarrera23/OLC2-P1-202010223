from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import TipoDato

from src.Symbol.ArrayInstancia import ArrayInstancia

from src.Symbol.Error import Error
from src.PatronSingleton.Singleton import Singleton


class DeclaracionArreglo(Instruccion):

    def __init__(self,idInstancia, expresion, linea, columna,dimensiones=None,mutable=False):
        self.idInstancia = idInstancia
        self.dimensiones = dimensiones
        self.expresion = expresion
        self.linea=linea
        self.columna=columna
        self.mutable=mutable

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        
        expresionArreglo = self.expresion.obtenerValor(entorno)
        if expresionArreglo.tipo != TipoDato.ARREGLO:
            raise Exception(s.addError(Error(f"La expresion necesita ser un arreglo",self.linea,self.columna)))
        if self.dimensiones==None:
            #print("sin dimensiones especificadas")
            objetoArreglo = expresionArreglo.valor


            if entorno.existeSimbolo(self.idInstancia):
                raise Exception(s.addError(Error(f"Variable ya existente con el nombre {self.idInstancia}",self.linea,self.columna)))

            objetoArreglo.identificador = self.idInstancia
            objetoArreglo.editable=self.mutable
            #print(objetoArreglo.valores)
            #print(objetoArreglo.dimensiones)
            #print(str(objetoArreglo.tipo))
            #print(str(objetoArreglo.editable))
            entorno.agregarSimbolo(objetoArreglo)
        else:
            #print("con dimensiones especificadas")
            D=self.dimensiones.obtenerValor(entorno)
            objetoArreglo = expresionArreglo.valor
            if objetoArreglo.tipo!=D.tipo:
                raise Exception(s.addError(Error(f"Tipo de datos no coinciden",self.linea,self.columna)))
            if entorno.existeSimbolo(self.idInstancia):
                raise Exception(s.addError(Error(f"Variable ya existente con el nombre {self.idInstancia}",self.linea,self.columna)))

            objetoArreglo.identificador = self.idInstancia
            objetoArreglo.editable=self.mutable
            #print(objetoArreglo.valores)
            #print(objetoArreglo.dimensiones)
            if D.valor!=objetoArreglo.dimensiones:
                raise Exception(s.addError(Error(f"Las dimensiones no son iguales con la expresion",self.linea,self.columna)))
            #print(str(objetoArreglo.tipo))
            #print(str(objetoArreglo.editable))
            entorno.agregarSimbolo(objetoArreglo)
            
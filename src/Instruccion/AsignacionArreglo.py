from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import TipoDato

from src.Symbol.ArrayInstancia import ArrayInstancia

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class AsignacionArreglo(Instruccion):
    def __init__(self,id,listaExpresiones, expresion, linea,columna):
        self.id=id
        self.listaExpresiones=listaExpresiones
        self.expresion=expresion
        self.linea=linea
        self.columna=columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        E=self.expresion.obtenerValor(entorno);
        #print("valor:",E.valor)
        if entorno.existeSimbolo(self.id) is not True:
            raise Exception(s.addError(Error(f"Arreglo {self.id} no existe",self.linea,self.columna)))

        arreglo = entorno.obtenerSimbolo(self.id)
        if isinstance(arreglo, ArrayInstancia) is not True:
            raise Exception(s.addError(Error(f"No es referencia de un arreglo",self.linea,self.columna)))
        #print(E.tipo, arreglo.tipo)

        if E.tipo!=arreglo.tipo:
            raise Exception(s.addError(Error(f"Los elementos del arreglo no son del mismo tipo",self.linea,self.columna)))
        # if len(self.listaExpresiones) != len(arreglo.dimensiones):
        #     print("Dimenciones variadas---------------")
        #     return RetornoType()

        dimensiones = []
        for d in self.listaExpresiones:
            dimension=d.obtenerValor(entorno)
            if dimension.tipo==TipoDato.I64 or dimension.tipo==TipoDato.USIZE:
                dimensiones.append(dimension.valor)
        #print(dimensiones)
        arreglo.Cambiar(dimensiones,0,arreglo.valores,E.valor)
        return
        
        
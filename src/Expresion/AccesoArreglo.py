
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato
from src.Symbol.ArrayInstancia import ArrayInstancia

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class AccesoArreglo(Expresion):
    def __init__(self, idArreglo, listaExpresiones, linea, columna):
        self.idArreglo = idArreglo
        self.listaExpresiones = listaExpresiones
        self.linea=linea
        self.columna=columna

    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        if entorno.existeSimbolo(self.idArreglo) is not True:
            raise Exception(s.addError(Error(f"Arreglo {self.id} no existe",self.linea,self.columna)))

        arreglo = entorno.obtenerSimbolo(self.idArreglo)
        if isinstance(arreglo, ArrayInstancia) is not True:
            raise Exception(s.addError(Error(f"No es referencia de un arreglo",self.linea,self.columna)))

        # if len(self.listaExpresiones) != len(arreglo.dimensiones):
        #     print("Dimenciones variadas---------------")
        #     return RetornoType()

        dimensiones = []
        for d in self.listaExpresiones:
            dimension=d.obtenerValor(entorno)
            if dimension.tipo==TipoDato.I64 or dimension.tipo==TipoDato.USIZE:
                dimensiones.append(dimension.valor)
        #print(dimensiones)
        valor = arreglo.obtenerValor(dimensiones,0,arreglo.valores)
        return RetornoType(valor = valor, tipo=arreglo.tipo)



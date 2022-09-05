
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato
from src.Symbol.ArrayInstancia import ArrayInstancia

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Symbol.Symbol import Simbolo

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
        
        print(arreglo)
        if isinstance(arreglo,Simbolo) ==True and isinstance(arreglo,ArrayInstancia)==False:
            dimensiones = []
            for d in self.listaExpresiones:
                dimension=d.obtenerValor(entorno)
                if dimension.tipo==TipoDato.I64 or dimension.tipo==TipoDato.USIZE:
                    dimensiones.append(dimension.valor)
            #print(dimensiones)
            if len(dimensiones)==1:
                #print(arreglo.valor[dimensiones[0]])
                return RetornoType(valor=arreglo.valor[dimensiones[0]],tipo=arreglo.tipo)
            if len(dimensiones)==2:
                #print(arreglo.valor[dimensiones[0]][dimensiones[1]])
                return RetornoType(valor=arreglo.valor[dimensiones[0]][dimensiones[1]],tipo=arreglo.tipo)
        
        
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



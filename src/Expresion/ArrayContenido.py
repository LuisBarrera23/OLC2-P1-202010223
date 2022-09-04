from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato
from src.Symbol.ArrayInstancia import ArrayInstancia

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error


class ArrayContenido(Expresion):

    def __init__(self, listaExpresiones,linea, columna):
        self.expresiones = listaExpresiones
        self.linea=linea
        self.columna=columna

    def obtenerValor(self, entorno) -> RetornoType:
        tipo = TipoDato.ERROR
        expresionesCompiladas = []
        s=Singleton.getInstance()

        # COMPILAR EXPRESIONES, OBTENER TAMAÑO DE CADA DIMENSION Y VALIDAR CONGRUENCIA DE TIPOS
        for i in range(0, len(self.expresiones)):
            expresion = self.expresiones[i]
            valorExpresion = expresion.obtenerValor(entorno)

            if i == 0:
                tipo = valorExpresion.tipo
                expresionesCompiladas.append(valorExpresion)
            else:
                if tipo != valorExpresion.tipo:
                    raise Exception(s.addError(Error(f"Los elementos del arreglo no son del mismo tipo",self.linea,self.columna)))
                else:
                    expresionesCompiladas.append(valorExpresion)

        
        # ahora creamos la data
        
        listaDimensiones  = []
        valores = []
        listaDimensiones.append(len(expresionesCompiladas)) # TAMAÑO DE LA DIMENSION 1
        tipoFinal = TipoDato.ERROR

        for i in range(0, len(expresionesCompiladas)):
            expresionCompilada = expresionesCompiladas[i]

            if expresionCompilada.tipo != TipoDato.ARREGLO:
                tipoFinal = expresionCompilada.tipo
                valores.append(expresionCompilada.valor)
                continue

            else:
                instanciaArray = expresionCompilada.valor
                if i == 0:
                    tipoFinal = instanciaArray.tipo
                    listaDimensiones.extend(instanciaArray.dimensiones)
                else:
                    if instanciaArray.tipo != tipoFinal: 
                        raise Exception(s.addError(Error(f"Los elementos del arreglo no son del mismo tipo",self.linea,self.columna)))

                valores.insert(i, instanciaArray.valores)


        instanciaArrayRetorno = ArrayInstancia(tipoFinal, listaDimensiones, valores)
        return RetornoType(valor=instanciaArrayRetorno,tipo=TipoDato.ARREGLO)
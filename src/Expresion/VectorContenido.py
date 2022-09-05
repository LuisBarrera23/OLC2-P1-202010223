from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato

class VectorContenido(Expresion):
    def __init__(self,tipodeclaracion, expresiones,linea,columna):
        self.tipodeclaracion=tipodeclaracion
        self.expresiones=expresiones
        self.linea=linea
        self.columna=columna

    def obtenerValor(self, entorno) -> RetornoType:
        if self.tipodeclaracion==1:
            iterador=0
            data=[]
            for i in self.expresiones:
                data.append(i.obtenerValor(entorno))
                

        return RetornoType()
        
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType,TipoDato

from src.Symbol.Error import Error
from src.PatronSingleton.Singleton import Singleton

class VectorContenido(Expresion):
    def __init__(self,tipodeclaracion, expresiones,linea,columna,capacidad=999,repeticiones=0):
        self.tipodeclaracion=tipodeclaracion
        self.expresiones=expresiones
        self.linea=linea
        self.columna=columna
        self.capacidad=capacidad
        self.repeticiones=repeticiones

    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        if self.tipodeclaracion==1:
            iterador=0
            data=[]
            for i in self.expresiones:
                actual=i.obtenerValor(entorno)
                if iterador==0:
                    tipo=actual.tipo
                    iterador=1
                    data.append(actual.valor)
                else:
                    if tipo==actual.tipo:
                        data.append(actual.valor)
                    else:
                        raise Exception(s.addError(Error(f"Las tipos no coinciden",self.linea,self.columna)))
            #print(data,tipo)
            return RetornoType(valor=data,tipo=tipo)
        elif self.tipodeclaracion==2:
            data=[]
            E1=self.expresiones.obtenerValor(entorno)
            tipo=E1.tipo
            E2=self.repeticiones.obtenerValor(entorno)
            if E2.tipo!=TipoDato.I64:
                raise Exception(s.addError(Error(f"El numero de repeticiones debe ser I64",self.linea,self.columna)))
            rep=E2.valor
            for i in range(rep):
                data.append(E1.valor)
            return RetornoType(valor=data,tipo=tipo)

        elif self.tipodeclaracion==3:
            data=[]
            tipo=None
            return RetornoType(valor=data,tipo=tipo)

        elif self.tipodeclaracion==4:
            data=[]
            tipo=None
            return RetornoType(valor=data,tipo=tipo)


        return RetornoType()
        
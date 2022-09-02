from src.Abstract.RetornoType import RetornoType
from src.Abstract.Instruccion import Instruccion
from src.Abstract.Expresion import Expresion

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Symbol.EntornoTabla import EntornoTabla

from src.Instruccion.Break import Break

class Loop(Instruccion,Expresion):
    def __init__(self, bloque, linea, columna):
        self.bloque=bloque
        self.linea=linea
        self.columna=columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        if self.bloque==[]:
            raise Exception(s.addError(Error("Loop Vacio",self.linea,self.columna)))
        
        bandera=True
        while bandera:
            nuevoEntorno=EntornoTabla(entorno)
            for i in self.bloque:
                retorno=i.Ejecutar(nuevoEntorno)
                if isinstance(retorno,Break):
                    if retorno.expresion==None:
                        bandera=False
                        break
                    else:
                        bandera=False
                        raise Exception(s.addError(Error("el break dentro de la instruccion loop no debe retornar nada",retorno.linea,retorno.columna)))


    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        if self.bloque==[]:
            s.addError(Error("Loop Vacio",self.linea,self.columna))
        bandera=True
        
        while bandera:
            nuevoEntorno=EntornoTabla(entorno)
            for i in self.bloque:
                retorno=i.Ejecutar(nuevoEntorno)
                if isinstance(retorno,Break):
                    if retorno.expresion==None:
                        raise Exception(s.addError(Error("el break dentro de la expresion loop debe retornar una expresion",retorno.linea,retorno.columna)))
                    else:
                        bandera=False
                        return retorno.Retorno
        return RetornoType()
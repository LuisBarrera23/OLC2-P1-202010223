from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType, TipoDato
from src.Abstract.Instruccion import Instruccion

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Instruccion.Funcion import Funcion
from src.Symbol.EntornoTabla import EntornoTabla
from src.Symbol.Symbol import Simbolo

from src.Instruccion.Return import Return

class Llamada(Instruccion,Expresion):
    def __init__(self,id, expresiones,linea, columna):
        self.id=id
        self.expresiones=expresiones
        self.linea=linea
        self.columna=columna

    def Ejecutar(self, entorno):
        return self.obtenerValor(entorno)

    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        existe=entorno.existeFuncion(self.id)
        if existe==False:
            raise Exception(s.addError(Error(f"La funcion {self.id} no existe",self.linea,self.columna)))

        funcion:Funcion=entorno.obtenerFuncion(self.id)
        # if funcion.tipo!=TipoDato.ERROR:
        #     raise Exception(s.addError(Error(f"La funcion {funcion.identificador} retorna un tipo de dato {self.strTipo(funcion.tipo)}",self.linea,self.columna)))
        nuevoEntorno=EntornoTabla(entorno)

        if funcion.parametros==[] and self.expresiones==[]:
            for i in funcion.bloque:
                retorno=i.Ejecutar(nuevoEntorno)
                if isinstance(retorno,Return):
                    if retorno.expresion==None:
                        if funcion.tipo!=TipoDato.ERROR:
                            raise Exception(s.addError(Error(f"El Return no esta retornando un tipo de dato {self.strTipo(funcion.tipo)}",retorno.linea,retorno.columna)))
                        return
                    else:
                        if funcion.tipo==TipoDato.ERROR:
                            raise Exception(s.addError(Error(f"La funcion {funcion.identificador} no debe de retornar ninguna expresion",retorno.linea,retorno.columna)))
                        if funcion.tipo==retorno.Retorno.tipo:
                            return retorno.Retorno
                        else:
                            raise Exception(s.addError(Error(f"El return necesita una expresion de tipo {self.strTipo(funcion.tipo)}",retorno.linea,retorno.columna)))
            if funcion.tipo!=TipoDato.ERROR:
                raise Exception(s.addError(Error(f"Falto implementar un return de tipo : {self.strTipo(funcion.tipo)}",funcion.linea,funcion.columna)))
            return

        self.compararParametros(nuevoEntorno,funcion.parametros,self.expresiones)
        for i in funcion.bloque:
            retorno=i.Ejecutar(nuevoEntorno)
            if isinstance(retorno,Return):
                if retorno.expresion==None:
                    if funcion.tipo!=TipoDato.ERROR:
                        raise Exception(s.addError(Error(f"El Return no esta retornando un tipo de dato {self.strTipo(funcion.tipo)}",retorno.linea,retorno.columna)))
                    return
                else:
                    if funcion.tipo==TipoDato.ERROR:
                        raise Exception(s.addError(Error(f"La funcion {funcion.identificador} no debe de retornar ninguna expresion",retorno.linea,retorno.columna)))
                    if funcion.tipo==retorno.Retorno.tipo:
                        return retorno.Retorno
                    else:
                        raise Exception(s.addError(Error(f"El return necesita una expresion de tipo {self.strTipo(funcion.tipo)}",retorno.linea,retorno.columna)))
        if funcion.tipo!=TipoDato.ERROR:
            raise Exception(s.addError(Error(f"Falto implementar un return de tipo : {self.strTipo(funcion.tipo)}",funcion.linea,funcion.columna)))
        
    def compararParametros(self, entornoN, parametros, expresiones):
        s=Singleton.getInstance()
        if len(parametros) != len(expresiones):
            raise Exception(s.addError(Error(f"No coincide la cantidad de parametros",self.linea,self.columna)))
        i=0
        for p in parametros:
            E:RetornoType=expresiones[i].obtenerValor(entornoN.padre)
            if E.tipo==p.tipo:
                nueva=Simbolo()
                nueva.Simbolo_primitivo(p.id,E.valor,E.tipo,self.linea,self.columna,True)
                entornoN.agregarSimbolo(nueva)
            else:
                raise Exception(s.addError(Error(f"Tipo de Parametro no coincide con los requeridos de la funcion",self.linea,self.columna)))
            i=i+1
        

    
    def strTipo(self,tipo:TipoDato)->str:
        if tipo==TipoDato.I64:
            return "I64"
        elif tipo==TipoDato.F64:
            return "F64"
        elif tipo==TipoDato.BOOL:
            return "BOOL"
        elif tipo==TipoDato.CHAR:
            return "CHAR"
        elif tipo==TipoDato.STRING:
            return "STRING"
        elif tipo==TipoDato.STR:
            return "&STR"
        elif tipo==TipoDato.USIZE:
            return "USIZE"
        elif tipo==TipoDato.ARREGLO:
            return "ARREGLO"
        return ""

    
        

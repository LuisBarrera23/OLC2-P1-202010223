from src.Abstract.RetornoType import RetornoType, TipoDato
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Abstract.Expresion import Expresion

class If_e(Expresion):
    def __init__(self,condicion, expresionPrincipal, listaelseif, expresionElse,linea,columna):
        self.condicion = condicion
        self.expresionPrincipal = expresionPrincipal
        self.listaelseif = listaelseif
        self.expresionElse = expresionElse
        self.linea=linea
        self.columna=columna

    def obtenerValor(self, entorno):
        s=Singleton.getInstance()
        #validamos que todas las condiciones sean booleanas

        CondicionPrincipal=self.condicion.obtenerValor(entorno)
        Principal=self.expresionPrincipal.obtenerValor(entorno)
        if CondicionPrincipal.tipo!=TipoDato.BOOL:
            raise Exception(s.addError(Error(f"Se necesita condiciones booleanas",self.linea,self.columna)))
        for elseif in self.listaelseif:
            print("holaaaaa1")
            condicionSecundaria=elseif.condicion.obtenerValor(entorno)
            Secundaria=elseif.expresionPrincipal.obtenerValor(entorno)
            print("holaaaaa2")
            if condicionSecundaria.tipo != TipoDato.BOOL:
                raise Exception(s.addError(Error(f"Se necesita condiciones booleanas",self.linea,self.columna)))
            if Secundaria.tipo != Principal.tipo:
                raise Exception(s.addError(Error(f"Todas las expresiones deben de ser del mismo tipo",self.linea,self.columna)))
        if self.expresionElse !=None:
            ValorElse=self.expresionElse.obtenerValor(entorno)
            if ValorElse.tipo != Principal.tipo:
                raise Exception(s.addError(Error(f"Todas las expresiones deben de ser del mismo tipo",self.linea,self.columna)))
        #ejecutamos y retornamos la opcion correcta
        print("holaaaaa3")
        if CondicionPrincipal.valor==True:
            return RetornoType(valor=Principal.valor,tipo=Principal.tipo)
        else:
            for elseif in self.listaelseif:
                condicionSecundaria=elseif.condicion.obtenerValor(entorno)
                Secundaria=elseif.expresionPrincipal.obtenerValor(entorno)
                if condicionSecundaria.valor==True:
                    return RetornoType(valor=Secundaria.valor,tipo=Secundaria.tipo)
            if self.expresionElse !=None:
                return RetornoType(valor=ValorElse.valor,tipo=ValorElse.tipo)
            return RetornoType()

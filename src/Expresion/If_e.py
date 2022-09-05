from src.Abstract.RetornoType import RetornoType, TipoDato
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Abstract.Expresion import Expresion
from src.Symbol.EntornoTabla import EntornoTabla

class If_e(Expresion):
    def __init__(self,condicion, expresionPrincipal, listaelseif, expresionElse,linea,columna,instruccion1=None,instruccion2=None):
        self.condicion = condicion
        self.expresionPrincipal = expresionPrincipal
        self.listaelseif = listaelseif
        self.expresionElse = expresionElse
        self.linea=linea
        self.columna=columna
        self.instruccion1=instruccion1
        self.instruccion2=instruccion2

    def obtenerValor(self, entorno):
        s=Singleton.getInstance()
        #validamos que todas las condiciones sean booleanas
        Nuevo=EntornoTabla(entorno)
        CondicionPrincipal=self.condicion.obtenerValor(entorno)
        #ejecutamos y retornamos la opcion correcta
        if CondicionPrincipal.valor==True:
            if self.instruccion1!=None:
                self.instruccion1.Ejecutar(entorno)
                Principal=self.expresionPrincipal.obtenerValor(entorno)
            else:
                Principal=self.expresionPrincipal.obtenerValor(entorno)
            return RetornoType(valor=Principal.valor,tipo=Principal.tipo)
        else:
            for elseif in self.listaelseif:
                condicionSecundaria=elseif.condicion.obtenerValor(entorno)
                
                if condicionSecundaria.valor==True:
                    if elseif.instruccion1!=None:
                        elseif.instruccion1.Ejecutar(entorno)
                        Secundaria=elseif.expresionPrincipal.obtenerValor(entorno)
                    else:
                        Secundaria=elseif.expresionPrincipal.obtenerValor(entorno)
                    return RetornoType(valor=Secundaria.valor,tipo=Secundaria.tipo)
            if self.expresionElse !=None:
                if self.instruccion2!=None:
                    self.instruccion2.Ejecutar(entorno)
                    ValorElse=self.expresionElse.obtenerValor(entorno)
                else:
                    ValorElse=self.expresionElse.obtenerValor(entorno)
                return RetornoType(valor=ValorElse.valor,tipo=ValorElse.tipo)
            return RetornoType()



        # Principal=self.expresionPrincipal.obtenerValor(entorno)
        # if CondicionPrincipal.tipo!=TipoDato.BOOL:
        #     raise Exception(s.addError(Error(f"Se necesita condiciones booleanas",self.linea,self.columna)))
        # for elseif in self.listaelseif:
        #     condicionSecundaria=elseif.condicion.obtenerValor(entorno)
        #     Secundaria=elseif.expresionPrincipal.obtenerValor(entorno)
        #     if condicionSecundaria.tipo != TipoDato.BOOL:
        #         raise Exception(s.addError(Error(f"Se necesita condiciones booleanas",self.linea,self.columna)))
        #     if Secundaria.tipo != Principal.tipo:
        #         raise Exception(s.addError(Error(f"Todas las expresiones deben de ser del mismo tipo",self.linea,self.columna)))
        # if self.expresionElse !=None:
        #     ValorElse=self.expresionElse.obtenerValor(entorno)
        #     if ValorElse.tipo != Principal.tipo:
        #         raise Exception(s.addError(Error(f"Todas las expresiones deben de ser del mismo tipo",self.linea,self.columna)))
        

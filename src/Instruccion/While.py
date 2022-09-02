from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import TipoDato,RetornoType

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Instruccion.Break import Break
from src.Instruccion.Continue import Continue
from src.Instruccion.Return import Return

from src.Symbol.EntornoTabla import EntornoTabla

class While(Instruccion):
    def __init__(self, condicion, bloque, linea, columna):
        self.condicion=condicion
        self.bloque=bloque
        self.linea=linea
        self.columna=columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        E1:RetornoType=self.condicion.obtenerValor(entorno)
        if E1.tipo!=TipoDato.BOOL:
            raise Exception(s.addError(Error(f"Instruccion while necesita una expresion booleana",self.linea,self.columna)))
        bandera=True
        
        while bandera:
            nuevoEntorno=EntornoTabla(entorno)
            condicion:RetornoType=self.condicion.obtenerValor(nuevoEntorno)
            if condicion.valor:
                for i in self.bloque:
                    retorno=i.Ejecutar(nuevoEntorno)
                    if isinstance(retorno,Continue):
                        break
                    elif isinstance(retorno,Return):
                        return retorno
                    elif isinstance(retorno, Break):
                        if retorno.expresion==None:
                            return
                        else:
                            raise Exception(s.addError(Error("Break en while no debe llevar expresiones",retorno.linea,retorno.columna)))
            else:
                return

from src.Abstract.Instruccion import Instruccion
from src.Abstract.RetornoType import RetornoType,TipoDato
from src.Symbol.EntornoTabla import EntornoTabla
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error
from src.Symbol.Symbol import Simbolo

from src.Instruccion.Break import Break
from src.Instruccion.Continue import Continue
from src.Instruccion.Return import Return

class For(Instruccion):
    def __init__(self, variable, valor1, valor2, tipofor, bloque,linea, columna):
        self.variable=variable
        self.valor1=valor1
        self.valor2=valor2
        self.tipofor=tipofor
        self.bloque=bloque
        self.linea=linea
        self.columna=columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        if self.tipofor==1:
            E1=self.valor1.obtenerValor(entorno)
            E2=self.valor2.obtenerValor(entorno)
            if E1.tipo!=TipoDato.I64 or E2.tipo!=TipoDato.I64:
                raise Exception(s.addError(Error(f"El rango del for necesita ser de tipo I64",self.linea,self.columna)))

            if E1.valor > E2.valor:
                raise Exception(s.addError(Error(f"El rango del for necesita ser ascendente",self.linea,self.columna)))

            for n in range(E1.valor,E2.valor):
                env=EntornoTabla(entorno)
                nuevo=Simbolo()
                nuevo.Simbolo_primitivo(self.variable,n,TipoDato.I64,self.linea,self.columna,True)
                env.agregarSimbolo(nuevo)
                retorno=None
                for i in self.bloque:
                    retorno=i.Ejecutar(env)
                    if isinstance(retorno,Return):
                        return retorno
                    elif isinstance(retorno,Break):
                        break
                    elif isinstance(retorno,Continue):
                        break
                if isinstance(retorno,Break):
                    if retorno.expresion==None:
                        return
                    else:
                        raise Exception(s.addError(Error("Break en ciclo for no debe llevar expresiones",retorno.linea,retorno.columna)))


        elif self.tipofor==2:
            E1=self.valor1.obtenerValor(entorno)
            if E1.tipo!=TipoDato.STR:
                raise Exception(s.addError(Error(f"For con chars necesita una expresion tipo STR",self.linea,self.columna)))

            for n in E1.valor:
                env=EntornoTabla(entorno)
                nuevo=Simbolo()
                nuevo.Simbolo_primitivo(self.variable,n,TipoDato.CHAR,self.linea,self.columna,True)
                env.agregarSimbolo(nuevo)
                retorno=None
                for i in self.bloque:
                    retorno=i.Ejecutar(env)
                    if isinstance(retorno,Return):
                        return retorno
                    elif isinstance(retorno,Break):
                        break
                    elif isinstance(retorno,Continue):
                        break
                if isinstance(retorno,Break):
                    if retorno.expresion==None:
                        return
                    else:
                        raise Exception(s.addError(Error("Break en ciclo for no debe llevar expresiones",retorno.linea,retorno.columna)))
        return
        
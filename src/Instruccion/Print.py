
from src.Abstract.RetornoType import TipoDato
from src.Abstract.Instruccion import Instruccion
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error


class Print(Instruccion):
    pass

    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea = linea
        self.columna = columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        E=self.expresion.obtenerValor(entorno)
        if(E.tipo==TipoDato.ERROR):
            raise Exception(s.addError(Error("Print fallido, revise la expresion",self.linea,self.columna)))
        #print(E.valor+" "+E.tipo)
        #print(E.valor,E.tipo,"linea", self.linea,"columna",self.columna)
        s.addConsola(str(E.valor)+"\n")

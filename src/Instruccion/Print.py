
from src.Abstract.Instruccion import Instruccion
from src.PatronSingleton.Singleton import Singleton


class Print(Instruccion):
    pass

    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea = linea
        self.columna = columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        E=self.expresion.obtenerValor(entorno)
        #print(E.valor+" "+E.tipo)
        print(E.valor,E.tipo,"linea", self.linea,"columna",self.columna)
        s.addConsola(str(E.valor)+"\n")

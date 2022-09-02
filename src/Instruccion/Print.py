
from cgi import print_arguments
from typing import List
from src.Abstract.RetornoType import RetornoType, TipoDato
from src.Abstract.Instruccion import Instruccion
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error


class Print(Instruccion):
    pass

    def __init__(self,expresion,linea,columna):
        self.expresion:List=expresion
        self.linea = linea
        self.columna = columna

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        # E=self.expresion.obtenerValor(entorno)
        # if(E.tipo==TipoDato.ERROR):
        #     raise Exception(s.addError(Error("Print fallido, revise la expresion",self.linea,self.columna)))
        if len(self.expresion)==1:
            s.addConsola(str(self.expresion[0].obtenerValor(entorno).valor)+"\n")
        else:
            lista=[]
            for i in self.expresion:
                lista.append(i.obtenerValor(entorno))
            formato=lista[0].valor
            lista.pop(0)
            estado=0
            salida=""
            for i in formato:
                if estado==0:
                    if i =="{":
                        estado=1
                    else:
                        salida+=i
                elif estado==1:
                    if self.isEspacio(i):
                        pass
                    elif i =="}":
                        if len(lista)>0:
                            salida+=str(lista[0].valor)
                            lista.pop(0)
                            estado=0
            s.addConsola(str(salida)+"\n")

    def isEspacio(self,c):
        if (ord(c)==32 or ord(c)==9 or ord(c)==10):
            return True
        else:
            return False

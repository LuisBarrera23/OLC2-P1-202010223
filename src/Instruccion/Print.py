
from cgi import print_arguments
from typing import List
from src.Abstract.RetornoType import RetornoType, TipoDato
from src.Abstract.Instruccion import Instruccion
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

from src.Symbol.ArrayInstancia import ArrayInstancia

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
                            if isinstance(lista[0].valor,ArrayInstancia):
                                salida+=str(lista[0].valor.valores)
                                lista.pop(0)
                            else:
                                salida+=str(lista[0].valor)
                                lista.pop(0)
                            estado=0
                    elif i ==":":
                        estado=2
                elif estado==2:
                    if i =="?":
                        estado=3
                    elif self.isEspacio(i):
                        pass
                elif estado==3:
                    if self.isEspacio(i):
                        pass
                    elif i=="}":
                        if len(lista)>0:
                            if isinstance(lista[0].valor,ArrayInstancia):
                                salida+=str(lista[0].valor.valores)
                                lista.pop(0)
                            else:
                                salida+=str(lista[0].valor)
                                lista.pop(0)
                            estado=0

            if len(lista)!=0:
                raise Exception(s.addError(Error("Print fallido, hicieron falta expresiones por imprimir",self.linea,self.columna)))
            s.addConsola(str(salida)+"\n")

    def isEspacio(self,c):
        if (ord(c)==32 or ord(c)==9 or ord(c)==10):
            return True
        else:
            return False

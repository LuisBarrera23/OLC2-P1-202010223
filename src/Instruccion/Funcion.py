from src.Abstract.Instruccion import Instruccion

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error


class Funcion(Instruccion):
    def __init__(self, identificador,tipo, bloque, parametros,linea,columna):
        self.identificador=identificador
        self.bloque=bloque
        self.parametros=parametros
        self.linea=linea
        self.columna=columna
        self.tipo=tipo

    def Ejecutar(self, entorno):
        s=Singleton.getInstance()
        existe=entorno.existeFuncion(self.identificador)
        if existe:
            raise Exception(s.addError(Error(f"La funcion {self.identificador} ya existe",self.linea,self.columna)))
        else:
            entorno.agregarFuncion(self)

    def Ejecutar_main(self,entorno):
        s=Singleton.getInstance()
        AST=self.bloque
        for i in AST:
            #i.Ejecutar(entorno)
            try:
                """"""
                i.Ejecutar(entorno)
            except:
                print("error")
        
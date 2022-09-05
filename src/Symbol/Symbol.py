from pickle import FALSE
from re import S
from src.Abstract.RetornoType import TipoDato

class Simbolo:

    def __init__(self):
        #PARA SIMBOLOS PRIMITIVOS
        self.identificador=""
        self.valor=None
        self.tipo= TipoDato.ERROR
        self.editable=False
        self.linea=0
        self.columna=0

        #EXTRA PARA FUNCIONES
        self.parametros=[]
        self.instrucciones=[]

        #EXTRA PARA ARREGLOS
        self.valores=[]
        self.dimensiones=[]
        
        #EXTRA PARA VECTORES
        self.capacidad=0

        
    def Simbolo_primitivo(self, id, valor,tipo,linea, columna, editable=False):
        self.identificador=id
        self.valor=valor
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        self.editable=editable
    
    def Simbolo_funcion(self, identificador, parametros, instrucciones, tipo=None):
        self.identificador=identificador
        self.parametros=parametros
        self.instrucciones=instrucciones
        self.tipo=tipo

    def Simbolo_arreglo(self,tipo, dimensiones, valores):
        self.tipo=tipo
        self.dimensiones=dimensiones
        self.valores=valores
        self.editable=False

    def Simbolo_vector(self,identificador,dimensiones,valor,capacidad,tipo,editable=False):
        self.identificador=identificador
        self.dimensiones=dimensiones
        self.valor=valor
        self.editable=editable
        self.capacidad=capacidad
        self.tipo=tipo

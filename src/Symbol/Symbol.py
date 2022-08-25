from pickle import FALSE
from src.Abstract.RetornoType import TipoDato

class Simbolo:

    def __init__(self):
        self.identificador=""
        self.valor=None
        self.tipo= TipoDato.ERROR
        self.editable=False
        self.linea=0
        self.columna=0

        
    def Simbolo_primitivo(self, id, valor,tipo,linea, columna, editable=False):
        self.identificador=id
        self.valor=valor
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        self.editable=editable
    
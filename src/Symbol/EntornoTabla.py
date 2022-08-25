from src.Symbol.Symbol import Simbolo


class EntornoTabla:
    def __init__(self,padre=None):
        self.padre=padre
        self.tabla={}
        self.tablafunciones={}
        self.tablaClases={}

    def existeSimbolo(self,identificador):
        entorno = self

        while entorno is not None:
            existe = entorno.tabla.get(identificador)
            if existe is not None:
                return True
            else:
                entorno = entorno.padre

        return False

    def existeSimboloEnEntornoActual(self,identificador):
        existe = self.tabla.get(identificador)
        if existe is not None:
            return True
        else:
            return False

    def obtenerSimbolo(self,identificador) -> Simbolo:
        entorno = self
        while entorno is not None:
            simbolo = entorno.tabla.get(identificador)
            if simbolo is not None:
                return simbolo
            else:
                entorno = entorno.padre

        return Simbolo()

    def agregarSimbolo(self, simboloAdd:Simbolo):
        self.tabla[simboloAdd.identificador] = simboloAdd

    def modificarSimbolo(self,identificador,valor):
        entorno = self
        while entorno is not None:
            simbolo:Simbolo = entorno.tabla.get(identificador)
            if simbolo is not None:
                simbolo.valor=valor
                return
            else:
                entorno = entorno.padre
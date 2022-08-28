class Parametro:
    def __init__(self, id, tipo, linea, columna, ref=False):
        self.id=id
        self.tipo=tipo
        self.ref=ref
        self.linea=linea
        self.columna=columna
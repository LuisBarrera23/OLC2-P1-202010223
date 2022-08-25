from datetime import datetime
class Error:
    def __init__(self,descripcion,linea,columna) -> None:
        self.descripcion=str(descripcion)
        self.linea=str(linea)
        self.columna=str(columna)
        actual=datetime.now()
        self.tiempo:str=actual.strftime("%d %B %Y %H:%M:%S")

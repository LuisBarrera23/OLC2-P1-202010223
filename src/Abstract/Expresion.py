from abc import ABC, abstractmethod

from src.Abstract.RetornoType import RetornoType

class Expresion(ABC):
    @abstractmethod
    def obtenerValor(self,entorno) -> RetornoType:
        pass
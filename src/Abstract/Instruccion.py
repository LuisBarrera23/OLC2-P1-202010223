from abc import ABC, abstractmethod

class Instruccion(ABC):
    @abstractmethod
    def Ejecutar(self, entorno):
        pass
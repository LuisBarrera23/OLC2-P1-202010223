from src.Symbol.Error import Error


class Singleton:

    __instance = None

   
    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        self.consola=""
        self.errores=[]
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    def reset(self):
        self.consola=""
        self.errores=[]

    def addConsola(self,texto):
        self.consola+=texto
    
    def getConsola(self)-> str:
        return self.consola

    def addError(self,Error:Error):
        self.errores.append(Error)
    
    def getErrores(self):
        return self.errores
    
from turtle import goto


class Singleton:

    __instance = None

   
    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        self.consola=""
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    def reset(self):
        self.consola=""

    def addConsola(self,texto):
        self.consola+=texto
    
    def getConsola(self)-> str:
        return self.consola
    
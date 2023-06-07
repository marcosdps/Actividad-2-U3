

class Sabor:
    __idSabor: int
    __ingredientes: str
    __nombreSabor: str


    def __init__(self, idSabor=None, ingredientes=None, nombreSabor=None):
        self.__idSabor = int(idSabor)
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor

    def getidSabor(self):
        return self.__idSabor
    
    def getIngredientes(self):
        return self.__ingredientes
    
    def getNombre(self):
        return self.__nombreSabor
    
    def __str__(self):
        return f"{self.__idSabor} {self.__ingredientes} {self.__nombreSabor}"
    
    
    
    

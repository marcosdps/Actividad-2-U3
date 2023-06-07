

class Helado:
    __gramos: float
    __precio: float
    __Sabor: list
    #un helado puede tener de 1 a 4 sabores


    def __init__(self, gramos=None, precio=None, sabor=None):
        self.__gramos = float(gramos)
        self.__precio = precio
        self.__Sabor = []

    def __str__(self):
        print(f"{self.__gramos} {self.__precio}")
        for i in range(len(self.__Sabor)):
            print(self.__Sabor[i])
    
    def getGramos(self):
        return self.__gramos
    
    def getPrecio(self):
        return self.__precio
    
    def agregarSabor(self, unSabor):
        self.__Sabor.append(unSabor)

    def mostrarDatos(self):
        print(f"{self.__gramos} {self.__precio}")
        for i in range(len(self.__Sabor)):
            print(self.__Sabor[i])

    def contarSabores(self, contadores):
        for i in range(len(self.__Sabor)):
            contadores[self.__Sabor[i].getidSabor()-1] +=1

    def buscarGramos(self,saborBuscado):
        i=0
        gramosBuscados = 0
        while i<len(self.__Sabor) and saborBuscado != self.__Sabor[i].getidSabor():
            i +=1
        if i < len(self.__Sabor):
            gramosBuscados = self.__gramos/len(self.__Sabor)
        return gramosBuscados
    
    def busquedaDeSabores(self,tipoBuscado):
        if tipoBuscado == self.__gramos:
            for i in range(len(self.__Sabor)):
                print(self.__Sabor[i].getNombre())


from ClaseSabor import Sabor
import numpy as np
import csv

class ManejaSabores:
    
    def __init__(self):
        self.__listaSabores = []

    def lecturaDatos(self):
        with open("sabores.csv", "r", encoding="utf8")as archi:
            reader = csv.reader(archi, delimiter=";")
            for fila in reader:
                self.__listaSabores.append(Sabor(*fila))

    
    def mostrarSabores(self):
        for i in range(len(self.__listaSabores)):
            print(f"codigo: {self.__listaSabores[i].getidSabor()}   Nombre: {self.__listaSabores[i].getNombre()}")

    def buscarDatos(self,ID):
        #unSabor = Sabor(ID-1,self.__listaSabores[ID-1].getIngredientes(), self.__listaSabores[ID-1].getNombre())
        unSabor = self.__listaSabores[ID-1]
        return unSabor
    
    def getCantidad(self):
        return len(self.__listaSabores)
    
    def mostrarSaboresMasPedidos(self,contadores, contOrdenados):
        print("Los 5 sabores mas pedidos son: ")
        for i in range(5):
            j=0
            while j < contadores.size and contOrdenados[i] != contadores[j]:
                j +=1
            print(self.__listaSabores[j].getNombre())
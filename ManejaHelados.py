from ClaseHelado import Helado
import numpy as np


class ManejaHelados:

    def __init__(self):
        self.__lista_H_Vendidos = []

    def registrarHelado(self, mSabores):
        print("Tipos de helados: 100gr, 150gr, 250gr, 500gr, 1000gr")
        gramosIce = float(input("Peso en gramos: "))
        precioIce = float(input("Precio: "))
        self.__lista_H_Vendidos.append(Helado(gramosIce,precioIce))
        mSabores.mostrarSabores()
        cantidad = int(input("Cuantos Sabores quiere agregar? Hasta 4 permitidos: "))
        if cantidad > 4:
            cantidad = 4
        elif cantidad < 1:
            cantidad = 1
        for i in range(cantidad):
            IDsaborIce = int(input("ID de sabor: "))
            unSabor = mSabores.buscarDatos(IDsaborIce)
            self.__lista_H_Vendidos[len(self.__lista_H_Vendidos)-1].agregarSabor(unSabor)

    def mostrarDatos(self):
        for i in range(len(self.__lista_H_Vendidos)):
            self.__lista_H_Vendidos[i].mostrarDatos()


    def saboresMasPedidos(self, mSabores):
        contadores = np.zeros(mSabores.getCantidad())
        for i in range(len(self.__lista_H_Vendidos)):
            self.__lista_H_Vendidos[i].contarSabores(contadores)
        contOrdenados = contadores
        contOrdenados = np.sort(contOrdenados)[::-1]#ordena el arreglo de menor a mayor y luego los invierte para que quede de mayor a menor
        mSabores.mostrarSaboresMasPedidos(contadores,contOrdenados)

    def gramosVendidos(self,saborBuscado):
        gramosVendidos = 0
        for i in range(len(self.__lista_H_Vendidos)):
            gramosVendidos += self.__lista_H_Vendidos[i].buscarGramos(saborBuscado)
        print(f"Se han vendido un total de {round(gramosVendidos,2)} del sabor ingresado")

    def buscarSaboresDeTipo(self,tipoBuscado):
        for i in range(len(self.__lista_H_Vendidos)):
            self.__lista_H_Vendidos[i].busquedaDeSabores(tipoBuscado)

    def calculoImporte(self):
        importes = np.zeros(5)
        for i in range(len(self.__lista_H_Vendidos)):
            match(self.__lista_H_Vendidos[i].getGramos()):
                case 100:
                    self.sumo(0,importes,i)
                case 150:
                    self.sumo(1,importes,i)
                case 250:
                    self.sumo(2,importes,i)
                case 500:
                    self.sumo(3,importes,i)
                case 1000:
                    self.sumo(4,importes,i)
        self.mostrarImportes(importes)

    def sumo(self,indice,importes, i):
        importes[indice] += self.__lista_H_Vendidos[i].getPrecio()

    def mostrarImportes(self, importes):
        print(f"Tipo 100: {importes[0]}\nTipo 150: {importes[1]}\nTipo 250: {importes[2]}\nTipo 500: {importes[3]}\nTipo 1000: {importes[4]}")


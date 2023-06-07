from ManejaHelados import ManejaHelados
from ManejaSabores import ManejaSabores
import os


if __name__ == "__main__":
    mHelados = ManejaHelados()
    mSabores = ManejaSabores()
    mSabores.lecturaDatos()
    os.system("cls")
    interfaz = """\n---------MENU DE OPCIONES---------
    -1- Registrar Helado vendido
    -2- Mostrar 5 sabores mas vendidos
    -3- Gramos vendidos de un sabor
    -4- Mostrar Sabores
    -5- Sabores vendidos de un tipo
    -6- Importe total por tipo
    -7- Mostrar Datos de ventas
    -0- SALIR"""
    print(interfaz)
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                print("\n-----Registrar Helado------\n")
                mHelados.registrarHelado(mSabores)
            case 2:
                print("\n-----5 sabores mas vendidos------\n")
                mHelados.saboresMasPedidos(mSabores)
            case 3: 
                print("\n-----Gramos vendidos de un sabor------\n")
                mSabores.mostrarSabores()
                saborBuscado = int(input("Ingrese un ID de sabor: "))
                mHelados.gramosVendidos(saborBuscado)
            case 4:
                print("\n-----LISTA DE SABORES------\n")
                mSabores.mostrarSabores()
            case 5:
                print("\n-----Sabores vendidos de un tipo------\n")
                tipoBuscado = float(input("Tipos de helados: 100gr, 150gr, 250gr, 500gr, 1000gr\nIngrese un tipo: "))
                mHelados.buscarSaboresDeTipo(tipoBuscado)
            case 6:
                print("\n-----Importe recaudado total por cada tipo de helado------\n")
                mHelados.calculoImporte()
            case 7:
                mHelados.mostrarDatos()

        print(interfaz)
        opcion = int(input("Ingrese una opcion: "))

import os
from os import system
import fnmatch
def accion1() :
    print("Listando archivos en el directorio actual:")
    system('ls')
def accion3():
    nombre_directorio = input("Ingresa el nombre del nuevo directorio: ")
    os.mkdir(nombre_directorio)
    print("Directorio "+nombre_directorio+" creado correctamente.")
def accion4():
    extension = input("Ingresa la extensión de archivo a buscar (txt,html):")
    for dirpath, dirnames, filenames in os.walk('/'):
        for filename in filenames:
            if fnmatch.fnmatch(filename, f'*.{extension}'):
                print(os.path.join(dirpath, filename))

def accion5():
    nombre_directorio=input("Ingresa la direccion de un directorio")
    total = 0
    for dirpath, dirnames, filenames in os.walk(nombre_directorio):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'rb') as file:
                print(f"Contando palabras en {filepath}")
                for line in file:
                    words = line.decode('ISO-8859-1').split()
                    total += len(words)
    print(f"El número total de palabras en el directorio {nombre_directorio} es {total}")
                      
def accion2():
    str = input("Ingrese la cadena a buscar en el nombre:")
    for dirpath, dirnames, filenames in os.walk('/'):
        for filename in filenames:
            if fnmatch.fnmatch(filename, f'*{str}*'):
                print(f"{os.path.join(dirpath, filename)} es un archivo")
        for dirname in dirnames:
            if fnmatch.fnmatch(dirname, f'*{str}*'):
                print(f"{os.path.join(dirpath, dirname)} es un directorio")

def printMenu():
    print("Seleccione una opción(0-5): ")
    print("0 - Salir")
    print("1 - Listar archivos y directorios del directorio actual")
    print("2 - Buscar archivos y directorios con una cadena")
    print("3 - Crear un directorio")
    print("4 - Buscar archivos con una extensión")
    print("5 - Número de palabras de cierto directorio")
def redFuncion(opcion):
    if(opcion==1):accion1()
    elif(opcion==2):accion2()
    elif(opcion==3):accion3()
    elif(opcion==4):accion4()
    elif(opcion==5):accion5()
opcion=-1

while(opcion!=0):
    printMenu()
    opcion = int(input())
    redFuncion(opcion)
    input("Press ENTER to continue")
    system('clear')
#!/usr/bin/python3
import os
from os import path



def ruta():
    
    print("============================================")
    directorio = str(input(" Introduce la ruta del directorio a listar: \n"
                           + "============================================\n"))
    if path.exists(directorio) :
        print(os.listdir(directorio))
    elif len(directorio) < 2:
        print("=======================")
        print("Ingrese una ruta válida")
        print("=======================")
    else: 
        print("===============================================")
        print("Directorio no existente, creado a la perfección")
        print("===============================================")
        os.makedirs(directorio)

def default():
    print("============================")
    print("Seleccione una opción válida")
    print("============================")

def imc():
    print("============================")
    peso = int(input(" Introduce tu peso (kg): \n"
                           + "============================\n"))
    print("==================================")
    altura = float(input(" Introduce tu altura (m): \n"
                           + "==================================\n"))
    imc = peso / (altura ** 2)
    print("================== \n"
          + "   Tabla IMC \n"
          + "================== \n"
          + "Peso bajo : < 18.5 \n"
          + "Peso medio: 18.5 > x > 24.9 \n"
          + "Sobrepeso: 25 > x > 29.9 \n"
          + "Obesidad: > 30 \n"
          + f"Tu imc es de {imc}")

def texto():
    nombre = str(input("Nombre del archivo: "))
    escribir = str(input("Escribe el texto que quieres dentro del archivo: "))

    ruta = os.getcwd()
    open("nombre.py", 'w').close()
    rutaArchivo = ruta + "/" + f"{nombre}"
    with open(f"{rutaArchivo}", "w") as archivo:
        archivo.write(escribir)
        

        
    eleccion = 1

while eleccion > 0 or eleccion < 5:
    
    eleccion = int(input("================================= \n" +
                        "| Seleccione la opción deseada: |\n" +
                        "================================= \n" +
                        "| 1) Listar/crear directorio    |\n" + 
                        "| 2) Calcular IMC               |\n" + 
                        "| 3) Escribir archivo           |\n" +
                        "| 4) Salir del menú             | \n" +
                        "================================= \n"))
    os.system("clear")
    match eleccion:
        case 1:
            ruta()
        case 2:
            imc()
        case 3:
            texto()
        case 4:
            os._exit(4)
        case other:
            default()
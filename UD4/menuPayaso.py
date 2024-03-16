#!/usr/bin/python3

# EJERCICIO MENU PYTHON
#Importamos la libreria que nos permite usar los comandos de navegación de debian en python

import shutil
import os
from os import system
from os import listdir

#______________________________________________________________

def limpiar_pantalla():
    
    system("clear")

#______________________________________________________________

def mostrar_menu():
    
    print("Menu de opciones:")
    print("1. Mostrar contenido de un directorio:")
    print("2. Crear un nuevo archivo:")
    print("3. Copiar un archivo a otro directorio:")
    print("4. Mostrar tamaño total del directorio:")
    print("5. Salir")

#______________________________________________________________

def mostrar_contenido_directorio():
    
    directorio = input("Ingrese la ruta del directorio: ")
    contenido = listdir(directorio)
    
    for item in contenido:
        print(item
#____________________________________el nombre__________________________

def copiar_archivo():
    )

#______________________________________________________________

def crear_nuevo_archivo():
    nombre_archivo = input("Ingrese el nombre del nuevo archivo: ")
    with open(nombre_archivo, 'w'):
        pass
    print("Archivo creado: ", nombre_archivo)

    archivo_origen = input("Ingrese  del archivo a copiar: ")
    
    directorio_destino = input("Ingrese el nombre del directorio donde quieres pegar el archivo: ")

    try:
        shutil.copy(archivo_origen, directorio_destino)
        print("Archivo copiado a", directorio_destino,": ")
        
    except FileNotFoundError:
        print("Archivo origen no encontrado")

#______________________________________________________________

def mostrar_tamano_directorio():
    
    directorio = input("Ingrese la ruta del directorio: ")
    
    if os.path.isdir(directorio):
        
        tamano = sum(os.path.getsize(os.path.join(directorio, archivo)) for archivo in os.listdir(directorio))
        print("El tamaño total del directorio", directorio, "es:", tamano, "Mb")
        
    else:
        print("El directorio", directorio, "no existe.")

#______________________________________________________________

continuar_ejecutando = True



while continuar_ejecutando:

    limpiar_pantalla()
    mostrar_menu()

    opcion = input("Ingrese su opción: ")

    if opcion == '1':
        mostrar_contenido_directorio()
        
    elif opcion == '2':
        crear_nuevo_archivo()
        
    elif opcion == '3':
        copiar_archivo()
        
    elif opcion == '4':
        mostrar_tamano_directorio()
        
    elif opcion == '5':
        
        print("Saliendo del programa. ¡Hasta luego!")
        continuar_ejecutando = False
        
    else:
        print("Opción inválida. Por favor, seleccione una opción dentro de los parámetros de ejecución")
    
    input("Introduce ENTER para continuar")
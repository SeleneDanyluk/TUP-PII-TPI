# Trabajo Práctico I - Programación II


import os
import bibloteca as biblio

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            biblio.prestar_ejemplar_libro()
            print() #tenemos que analizar si lo dejamos
        elif int(opt) == 2:
            biblio.devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            nuevo_libro = biblio.registrar_nuevo_libro()
            print(nuevo_libro['cod'], nuevo_libro['cant_ej_ad'], nuevo_libro['cant_ej_pr'], nuevo_libro['titulo'], nuevo_libro['autor'])
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")
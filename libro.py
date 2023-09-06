# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

import cod_generator as generador_cod

def nuevo_libro():
    codigo = generar_codigo()
    cant_ad = int(input("Ingrese la cantidad de ejemplares: "))
    cant_pr = int(input("Ingrese la cantidad de ejemplares prestados"))
    title = input("Ingrese el título del libro")
    autor_libro = input("Ingrese el autor del libro")
    
    libro = {'cod': codigo, 'cant_ej_ad': cant_ad, 'cant_ej_pr': cant_pr, "titulo": title, "autor": autor_libro}
    
    return libro

def generar_codigo():
    return generador_cod.generar()
    

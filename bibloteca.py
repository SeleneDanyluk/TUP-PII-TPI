import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        if libro['cant_ej_pr'] > 0 :
            print(f"{libro['cod']} - {libro['titulo']} - Cantidad de ejemplares prestados: {libro['cant_ej_pr']}")
        elif libro['cant_ej_pr'] == 0:
            print(f"El libro {libro['titulo']} no tiene ejemplares prestados.")
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    return nuevo_libro

def eliminar_ejemplar_libro():
    #consultar si es un solo ejemplar o le pedimos al usuario que ingrese la cantidad.
    codigo = input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo:
            libro['cant_ej_ad'] -= 1
            print(f"La cantidad de ejemplares adquiridos del libro {libro['titulo']} actualizada es: {libro['cant_ej_ad']}") 
            return None
    
    print("Error! El código ingresado no existe.")
    return None

def prestar_ejemplar_libro():
    codigo = input("Ingrese el código del libro: ")

    for libro in libros:
        if libro['cod'] == codigo:
            print(f"\nAutor: {libro['autor']}")
            print(f"Titulo: {libro['titulo']}")
            print(f"Cantidad de ejemplares disponibles: {libro['cant_ej_ad']- libro['cant_ej_pr']}")

            if libro['cant_ej_ad'] - libro['cant_ej_pr'] < 1:
                print("No quedan ejemplares disponibles para realizar el prestamo")
            else:
                print("Prestamo confirmado!")
                libro['cant_ej_pr'] = libro['cant_ej_pr'] + 1
            return None
    print("Error! El código ingresado no existe.")
    return None

def devolver_ejemplar_libro():
    codigo = input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo:

            if  libro['cant_ej_pr'] >= 1:
                print("Se realizó la devolución correctamente.")
                libro['cant_ej_pr'] = libro['cant_ej_pr'] - 1
            else:
                print("Error! Este libro no posee ejemplares prestados.")
            return None
    print("Error! El codigo ingresado no existe.")
    return None

def mostrar_libro(libro):
    print(f"Código: {libro['cod']}")
    print(f"Ejemplares adquiridos: {libro['cant_ej_ad']}")
    print(f"Ejemplares prestados: {libro['cant_ej_pr']}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
def ingreso_de_datos ():
    nombre_apellido = input("Ingrese su nombre y apellido: ")
    dni = int(input("Ingrese su DNI: "))
    ciudad = str(input("Ingrese ciudad en donde vive: "))
    nuevo_pasajero = (nombre_apellido, dni, ciudad)
    
    guardar_pasajero (nuevo_pasajero)

def guardar_pasajero (nuevo_pasajero):
    pasajeros_lista.append((nuevo_pasajero))
    return pasajeros_lista

def menu (opcion):
    while opcion == 1:
        ingreso_de_datos()
        print("Quiere continuar ingresando pasajeros?")
        print("---------------------------------------------")
        print("0 - Salir")
        print("1 - Continuar ingresando")
        opcion = int(input("Ingrese una opcion: "))
        print("------------------------------------------------")
        print(pasajeros_lista)

    print("Adiosito")

pasajeros_lista = []
opcion = 1

menu(opcion)




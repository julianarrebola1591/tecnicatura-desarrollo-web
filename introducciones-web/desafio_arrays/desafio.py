def ingresar_pasajero (ciudades_lista):
    nombre_apellido = input("Ingrese su nombre y apellido: ")
    dni = int(input("Ingrese su DNI: "))
    ciudad = str(input("Ingrese ciudad en donde viaja: "))
    nuevo_pasajero = (nombre_apellido, dni, ciudad) #Falta ingresar la provincia correspondiente a la ciudad
    
    guardar_pasajero (nuevo_pasajero)

def ingresar_ciudad():
    provincia = str(input("Ingrese provincia: "))
    ciudad = str(input("Ingrese ciudad: "))
    nuevo_ciudad = (ciudad, provincia)
    guardar_ciudad (nuevo_ciudad)

def guardar_pasajero (nuevo_pasajero):
    pasajeros_lista.append((nuevo_pasajero))
    return pasajeros_lista

def guardar_ciudad (nuevo_ciudad):
    ciudades_lista.append((nuevo_ciudad))

def menu (opcion):
    while opcion != 0:
        print("Sistema de viajes")
        print("---------------------------------------------")
        print("0 - Salir")
        print("1 - Ingresar una nuevo pasajero")
        print("2 - Agregar una ciudad nueva")
        print("3 - Buscar pasajero por DNI")
        print("4 - Ver la cantidad de pasajeros por ciudad")
        print("5 - Ver la cantidad de pasajeros por provincia")        
        print("------------------------------------------------")
        print("6 - Ver listado de pasajeros")
        print("7 - Ver listado de ciudades")
        print(pasajeros_lista)
        print(ciudades_lista)
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            ingresar_pasajero()
        elif opcion == 2:
            ingresar_ciudad()
        print("Adiosito")

pasajeros_lista = []
ciudades_lista = []
opcion = 1

menu(opcion)




def ingresar_pasajero (ciudades_lista):
    nombre_apellido = input("Ingrese su nombre y apellido: ")
    dni = int(input("Ingrese su DNI: "))
    ciudad = str(input("Ingrese ciudad en donde viaja: "))
    for i in ciudades_lista:
        if i[0] == ciudad:
            provincia = i[1]
    nuevo_pasajero = (nombre_apellido, dni, ciudad, provincia) #Falta ingresar la provincia correspondiente a la ciudad
    
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

def buscar_DNI (pasajeros_lista):
    dni_busqueda = int(input("Ingrese el DNI del pasajero"))
    for pasajero in pasajeros_lista:
        if dni_busqueda == pasajero[1]:
            print(pasajero)

def contar_pasajeros(pasajeros_lista):
    ciudad_busqueda = str(input("Ingrese una ciudad: "))
    contador = 0
    for pasajero in pasajeros_lista:
        if pasajero[2] == ciudad_busqueda:
            contador += 1
    print(contador)

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
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            ingresar_pasajero(ciudades_lista)
            print(pasajeros_lista)
        elif opcion == 2:
            ingresar_ciudad()
            print(ciudades_lista)
        elif opcion == 3:
            buscar_DNI(pasajeros_lista)
            input("Precionar para una tecla continuar...")
        elif opcion == 4:
            contar_pasajeros(pasajeros_lista)
            input("Precionar para una tecla continuar...")
        else:
            print("Adiosito")

pasajeros_lista = [
    ("Julian Arrebola"),("41511891"),("Rosario"),("Santa Fe")
]
ciudades_lista = [
    ("Rosario", "Santa Fe") ,
    ("Bariloche", "Rio Negro")
    ]
opcion = 1

menu(opcion)




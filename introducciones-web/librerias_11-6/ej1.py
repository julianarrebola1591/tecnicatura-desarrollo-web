import random

opcion = 1

def crear_lista_aleatoria():
    lista_aleatoria = []
    for i in range(10):
        lista_aleatoria.append(random.randint(1,10))
    return lista_aleatoria

def ordenar_lista(lista_aleatoria : list) -> list:
    lista_ordenada = lista_aleatoria.copy()

#    for num1 in lista_aleatoria:
#        for i in len(lista_aleatoria):
#            if num1 < lista_aleatoria[i]:
#                lista_ordenada[num1] = INTENTAR ORDENAR LA LISTA A MANO
    return lista_ordenada

def menu (opcion):
    while opcion != 0:
        print("Sistema de viajes")
        print("---------------------------------------------")
        print("0 - Salir")
        print("1 - Armar una lista de 10 numeros aleatorios")
        print("2 - Ordenar la lista")

        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            lista_aleatoria = crear_lista_aleatoria()
            print(lista_aleatoria)
        elif opcion == 2:
            lista_ordenara = ordenar_lista(lista_aleatoria)
            print(lista_ordenara)
        else:
            print("Adiosito")

menu(opcion)

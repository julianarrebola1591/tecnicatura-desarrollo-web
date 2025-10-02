from ManejadorArma import ManejadorArma
from ManejadorPersonaje import ManejadorPersonaje
# Guardando el contenido de los CSV en listas
import csv
def importarCsv(ruta):
    with open(ruta, newline="", encoding="utf-8") as file:
        lista = []
        listaFinal = []
        jugadoresCSV = csv.reader(file)
        for fila in jugadoresCSV:
            for i in fila:
                lista.append(i)
            listaFinal.append(lista)
            lista = []
        return listaFinal
    
nombres = importarCsv("csvArmas/nombres_personajes.csv")
adjetivos = importarCsv("csvArmas/adjetivos_personajes.csv")

#PROGRAMA PRINCIPAL
personajes = ManejadorPersonaje(2, 2)

personajes.crearPersonajes(nombres, adjetivos)
personajes.configurarArsenal()
personajes.listarPersonajes()
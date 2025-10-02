import random
from Arma import Arma


# Guardando el contenido de los CSV en listas

import csv

def importarCsv(ruta):
    with open(ruta, newline="", encoding="utf-8") as file:
        lista = []
        jugadoresCSV = csv.reader(file)
        for fila in jugadoresCSV:
            for i in fila:
                lista.append(i)
        return lista
    
prefijos = importarCsv("csvArmas/prefijos.csv")
sufijos = importarCsv("csvArmas/sufijos_opcionales.csv")
base = importarCsv("csvArmas/base.csv")

class ManejadorArma:
    def __init__ (self, cantidad_armas:int):
        self.__cantidad_armas = cantidad_armas
        self.__lista_de_armas = []
        
    @property
    def cantidad_armas(self):
        return self.__cantidad_armas
    
    @cantidad_armas.setter
    def cantidad_armas(self, nuevaCantidad_armas:int):
        self.__cantidad_armas = nuevaCantidad_armas 
        
    @property
    def lista_de_armas(self):
        return self.__lista_de_armas
    
    @lista_de_armas.setter
    def lista_de_armas(self, nuevaLista_de_armas:list):
        self.__lista_de_armas = nuevaLista_de_armas
    
    def crearArmaAleatoria(self, prefijos, sufijos, base):
        nombre = random.choice(prefijos) + " " + random.choice(base) + " " + random.choice(sufijos)
        tipo = random.choice(["Ofensivo", "Defensivo"])
        puntos_fuerza = random.randint(1, 100)
        puntos_resistencia = random.randint(1, 100)
        usa_mana = random.choice([True, False])
        ventaja_sobre = random.choice(["Dragon, Elfo, Guerrero"])
        return Arma(nombre, tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventaja_sobre)
    
    def listarArmas(self):
        print("Listado de armas:")
        for arma in self.__lista_de_armas:
            print(f"{arma.nombre} -> \t Tipo: {arma.tipo}, Puntos de Fuerza: {arma.puntos_fuerza}, Puntos de Resistencia: {arma.puntos_resistencia}, Usa Mana: {arma.usa_mana}, Ventaja sobre: {arma.ventaja_sobre}")
    
    def crearArmas(self):
        self.__lista_de_armas = []
        for i in range(self.__cantidad_armas):
            arma = self.crearArmaAleatoria(prefijos, sufijos, base)
            self.__lista_de_armas.append(arma)
        return
    
#arsenal = ManejadorArma(5)
#arsenal.crearArmas()
#arsenal.listarArmas()
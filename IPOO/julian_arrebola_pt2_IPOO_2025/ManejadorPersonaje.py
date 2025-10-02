import random
from Personaje import Personaje
from ManejadorArma import ManejadorArma
from Guerrero import Guerrero
from Dragon import Dragon
from Elfo import Elfo




class ManejadorPersonaje:
    def __init__ (self, cantidad_personajes:int, cantidad_armas:int = 1):
        self.__cantidad_personajes = cantidad_personajes
        self.__lista_de_personajes = []
        self.__cantidad_armas = cantidad_armas
        
    @property
    def cantidad_personajes(self):
        return self.__cantidad_personajes
    
    @cantidad_personajes.setter
    def cantidad_personajes(self, nuevaCantidad_personajes:int):
        if nuevaCantidad_personajes < 1 or nuevaCantidad_personajes > 10:
            print("La cantidad de personajes debe ser entre 1 y 10")
            return
        self.__cantidad_personajes = nuevaCantidad_personajes
    
    @property
    def lista_de_personajes(self):
        return self.__lista_de_personajes
    
    @lista_de_personajes.setter
    def lista_de_personajes(self, nuevaLista_de_personajes:list):
        self.__lista_de_personajes = nuevaLista_de_personajes
        
    @property
    def cantidad_armas(self):
        return self.__cantidad_armas
    
    @cantidad_armas.setter
    def cantidad_armas(self, nuevaCantidad_armas:int):
        if nuevaCantidad_armas < 1 or nuevaCantidad_armas > 5:
            print("La cantidad de armas debe ser entre 1 y 5")
            return
        self.__cantidad_armas = nuevaCantidad_armas 
        
    
    def crearPersonajeAleatorio(self, nombres, adjetivos):
        clase = random.choice([Guerrero, Dragon, Elfo])
        genero = random.choice(["Masculino", "Femenino"])
        #falta filtrar nombres por genero
        nombre = random.choice(nombres)[0] + " " + random.choice(adjetivos)[0]
        puntosVida = random.randint(50, 100)
        puntosAtaque = random.randint(30, 80)
        puntosDefensa = random.randint(20, 70)
        if clase == Guerrero:
            armadura = random.randint(5, 20)
            return Guerrero(nombre,puntosVida, puntosAtaque, puntosDefensa, armadura)
        elif clase == Dragon:
            mana = random.randint(20, 50)
            elemento = random.choice(["Fuego", "Hielo", "Rayo"])
            return Dragon(nombre,puntosVida, puntosAtaque, puntosDefensa, mana, elemento)
        elif clase == Elfo:
            regeneracion = random.randint(1, 10)
            mana = random.randint(10, 30)
            return Elfo(nombre,puntosVida, puntosAtaque, puntosDefensa, mana, regeneracion)
        
    def configurarArsenal (self):
        for personaje in self.__lista_de_personajes:
            manejador_armas = ManejadorArma(self.__cantidad_armas)
            manejador_armas.crearArmas()
            personaje.arsenal = manejador_armas.lista_de_armas
        return
    
    def crearPersonajes(self, nombres, adjetivos):
        self.__lista_de_personajes = []
        for i in range(self.__cantidad_personajes):
            personaje = self.crearPersonajeAleatorio(nombres, adjetivos)
            self.__lista_de_personajes.append(personaje)
        return
    
    def listarPersonajes(self):
        for personajeAleatorio in self.lista_de_personajes:
            print("Detalles del personaje aleatorio creado:")
            print(f"Clase: {personajeAleatorio.__class__.__name__}")
            print(f"Nombre: {personajeAleatorio.nombre}")
            print(f"Puntos de Vida: {personajeAleatorio.puntosVida}")
            print(f"Puntos de Ataque: {personajeAleatorio.puntosAtaque}")
            print(f"Puntos de Defensa: {personajeAleatorio.puntosDefensa}")
            print(f"Habilidades: {personajeAleatorio.habilidades}")
            print(f"Debilidades: {personajeAleatorio.debilidades}")

            if isinstance(personajeAleatorio, Guerrero):
                print(f"Armadura: {personajeAleatorio.armadura}")
            elif isinstance(personajeAleatorio, Dragon):
                if personajeAleatorio.mana:
                    print(f"Mana: Si")
                else: print(f"Mana: No")
                print(f"Elemento: {personajeAleatorio.elemento}")
            elif isinstance(personajeAleatorio, Elfo):
                print(f"Mana: {personajeAleatorio.mana}")
                print(f"Regeneración: {personajeAleatorio.regeneracion}")
                
            for arma in personajeAleatorio.arsenal:
                print(f"  - Arma: {arma.nombre}, Tipo: {arma.tipo}, Puntos de Fuerza: {arma.puntos_fuerza}, Puntos de Resistencia: {arma.puntos_resistencia}, Usa Mana: {arma.usa_mana}, Ventaja sobre: {arma.ventaja_sobre}")
            print("\n")
            print("----------------------------------------")
            print("\n")
        return





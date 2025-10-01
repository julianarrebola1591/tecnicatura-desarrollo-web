from Personaje import Personaje

class Guerrero(Personaje):
    def __init__(self,armadura : int=10):
        super().__init__(nombre="Guerrero sin nombre", puntos_vida=10, puntos_ataque=10, puntos_defensa=5)
        self.__armadura = armadura
        self.habilidades = ["Usar dos armas", "Ataque doble", "Esquivo"]
        self.debilidades = ["Magia", "Dragón"]
    
    @property
    def armadura(self):
        return self.__armadura
    
    @armadura.setter
    def armadura(self, nueva_armadura:int):
        self.__armadura = nueva_armadura
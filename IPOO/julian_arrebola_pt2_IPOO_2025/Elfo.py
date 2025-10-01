from Personaje import Personaje

class Elfo(Personaje):
    def __init__(self,mana:int=10, regeneracion:int=1):
        super().__init__(nombre="Elfo sin nombre", puntos_vida=30, puntos_ataque=5, puntos_defensa=10)
        self.__mana = mana
        self.__regeneracion = regeneracion
        self.habilidades = ["Ataque Rápido", "Doble ráfaga"]
        self.debilidades = ["Dragones", "Oscuridad"]
        
    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana(self, nuevo_mana:int):
        self.__mana = nuevo_mana
        
    @property
    def regeneracion(self):
        return self.__regeneracion
    
    @regeneracion.setter
    def regeneracion(self, nueva_regeneracion:int):
        self.__regeneracion = nueva_regeneracion
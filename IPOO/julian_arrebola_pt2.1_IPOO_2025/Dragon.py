from Personaje import Personaje

class Dragon(Personaje):
    def __init__(self, nombre, puntos_vida=75, puntos_ataque=25, puntos_defensa=25, mana:int=25, elemento:str="Fuego"):
        super().__init__(nombre=nombre, puntos_vida=puntos_vida, puntos_ataque=puntos_ataque, puntos_defensa=puntos_defensa)
        self.__mana = mana
        self.__elemento = elemento
        self.habilidades = ["Invocación oscura", "Embestida mortal"]
        self.debilidades = ["Magia", "Luz"]
        
    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana(self, nuevo_mana:int):
        self.__mana = nuevo_mana
        
    @property
    def elemento(self):
        return self.__elemento
    
    @elemento.setter
    def elemento(self, nuevo_elemento:str):
        self.__elemento = nuevo_elemento
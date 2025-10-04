from Arma import Arma

class Espada(Arma):
    #Constructor
    def __init__(self, gemas:list = []):
        super().__init__(nombre = "Espada", tipo = "Ofensivo", puntos_fuerza = 10, puntos_resistencia = 0, usa_mana = False, ventaja_sobre = "Dragon")
        self.__gemas = []
        print("Espada creada correctamente")
        
    #Getters y Setters
    @property
    def gemas(self):
        return self.__gemas
    
    @gemas.setter
    def gemas(self, nuevas_gemas:list):
        self.__gemas = nuevas_gemas
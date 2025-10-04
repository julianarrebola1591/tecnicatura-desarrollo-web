from Arma import Arma

class Arco(Arma):
    #Constructor
    def __init__(self, cant_flechas:int = 10):
        super().__init__(nombre = "Arco", tipo = "Ofensivo", puntos_fuerza = 5, puntos_resistencia = 0, usa_mana = False, ventaja_sobre = "Dragon")
        self.__cant_flechas = cant_flechas
        print("Arco creada correctamente")
        
    #Getters y Setters
    @property
    def cant_flechas(self):
        return self.__cant_flechas
    
    @cant_flechas.setter
    def gemas(self, cant_flechas:list):
        self.__cant_flechas = cant_flechas
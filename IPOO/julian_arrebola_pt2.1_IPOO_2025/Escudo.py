from Arma import Arma

class Escudo(Arma):
    #Constructor
    def __init__(self, aumento_resistencia:int = 1,):
        super().__init__(nombre = "Escudo", tipo = "Defensivo", puntos_fuerza = 15, puntos_resistencia = 100, usa_mana = False, ventaja_sobre = "Elfo")
        self.puntos_resistencia = self.puntos_resistencia * aumento_resistencia
        print("Escudo creada correctamente")
        
    #Getters y Setters
    @property
    def puntos_resistencia(self):
        return self.__puntos_resistencia
    
    @puntos_resistencia.setter
    def puntos_resistencia(self, puntos_resistencia:list):
        self.__puntos_resistencia = puntos_resistencia
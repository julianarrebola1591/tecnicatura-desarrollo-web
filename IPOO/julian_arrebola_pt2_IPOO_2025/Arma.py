class Arma:
    
    #Constructor
    def __init__(self, nombre:str, tipo:str = "Espada", puntos_fuerza:int = 1, puntos_resistencia:int = 1, usa_mana:bool =  False, ventaja_sobre:str = ""):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__puntos_fuerza = puntos_fuerza
        self.__puntos_resistencia = puntos_resistencia
        self.__usa_mana = usa_mana
        self.__ventaja_sobre = ventaja_sobre

        
    #Getters y Setters
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, nuevo_tipo:str):
        self.__tipo = nuevo_tipo
        
    @property
    def puntos_fuerza(self):
        return self.__puntos_fuerza
    
    @puntos_fuerza.setter
    def puntos_fuerza(self, nuevos_puntos_fuerza:int):
        self.__puntos_fuerza = nuevos_puntos_fuerza
        
    @property
    def puntos_resistencia(self):
        return self.__puntos_resistencia
    
    @puntos_resistencia.setter
    def puntos_resistencia(self, nuevos_puntos_resistencia:int):
        self.__puntos_resistencia = nuevos_puntos_resistencia
        
    @property
    def usa_mana(self):
        return self.__usa_mana
    
    @usa_mana.setter
    def usa_mana(self, nuevo_usa_mana:bool):
        self.__usa_mana = nuevo_usa_mana
        
    @property
    def ventaja_sobre(self):
        return self.__ventaja_sobre
    
    @ventaja_sobre.setter
    def ventaja_sobre(self, nueva_ventaja_sobre:str):
        self.__ventaja_sobre = nueva_ventaja_sobre
        
#Metodos
def atacar(self):
    print(f"{self.__nombre} tiene {self.__puntos_fuerza} puntos de fuerza")

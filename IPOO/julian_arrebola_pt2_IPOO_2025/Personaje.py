class Personaje:
   
    #Constructor
    def __init__(self, nombre:str = "Personaje sin nombre",  puntosVida:int = 10, puntosAtaque:int = 10, puntosDefensa:int = 5):
        self.__nombre = nombre
        self.__puntosVida = puntosVida
        self.__puntosAtaque = puntosAtaque
        self.__puntosDefensa = puntosDefensa
        print("Personaje creado correctamente")
        
        #Getters y Setters
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre:int):
        self.__nombre = nuevoNombre
        
    @property
    def puntosVida(self):
        return self.__puntosVida
    
    @puntosVida.setter
    def puntosVida(self, nuevosPuntosVida:int):
        self.__puntosVida = nuevosPuntosVida
        
    @property
    def puntosAtaque(self):
        return self.__puntosAtaque
    
    @puntosAtaque.setter
    def puntosAtaque(self, nuevosPuntosAtaque:int):
        self.__puntosAtaque = nuevosPuntosAtaque
        
    @property
    def puntosDefensa(self):
        return self.__puntosDefensa
    
    @puntosDefensa.setter
    def puntosDefensa(self, nuevosPuntosDefensa:int):
        self.__puntosDefensa = nuevosPuntosDefensa

        
#Metodos

    def atacar(self):
        print(self.__puntosAtaque)

    def defender(self,recibeDaño:int, ) -> bool:
        if self.__puntosVida <= 0:
            return False
        else:
            self.__puntosVida = (self.puntosVida - recibeDaño)
            return True

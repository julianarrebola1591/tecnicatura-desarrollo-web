from Arma import Arma


class Personaje:
   
    #Constructor
    def __init__(self, nombre:str = "Personaje sin nombre",  puntos_vida:int = 10, puntos_ataque:int = 10, puntos_defensa:int = 5):
        self.__nombre = nombre
        self.__puntosVida = puntos_vida
        self.__puntosAtaque = puntos_ataque
        self.__puntosDefensa = puntos_defensa
        self.__arsenal = []
        
    
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
        
    @property
    def arsenal(self):
        return self.__arsenal
    
    @arsenal.setter
    def arsenal(self, nuevoArsenal:list):
        self.__arsenal = nuevoArsenal

        
#Metodos

    def atacar(self):
        print(self.__puntosAtaque)

    def defender(self,recibeDaño:int, ) -> bool:
        if self.__puntosVida <= 0:
            return False
        else:
            self.__puntosVida = (self.puntosVida - recibeDaño)
            return True

    def agregarArma (self, arma:Arma):
        if len(self.__arsenal) > 5:
            print("No se pueden agregar mas armas")
            return
        for a in self.__arsenal:
            if a.nombre == arma.nombre:
                print("El arma ya existe en el arsenal")
                return
        self.__arsenal.append(arma)
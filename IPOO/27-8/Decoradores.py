class Personaje:
   
    #Constructor
    def __init__(self, nombre:str = "Personaje sin nombre", puntosVida:int = 10, puntosAtaque = 7, puntosDefensa:int = 5):
        self.nombre = nombre
        self.__puntosVida = puntosVida  #Con el __ Determinamos que el atributo es PRIVADO - Debemos usar el getter para obtener el valor
        self.puntosAtaque = puntosAtaque
        self.puntosDefensa = puntosDefensa
        print("Personaje creado correctamente")
        
    @property
    def puntosVida(self):
        return self.__puntosVida

    @puntosVida.setter
    def setPuntosVida(self, puntosVida:int) -> None:
        if puntosVida > 0:
            self.__puntosVida = puntosVida

        


orco = Personaje()
print(f"Nombre: {orco.nombre}, Puntos de vida: {orco.puntosVida}, Puntos de ataque: {orco.puntosAtaque}, Puntos de defensa: {orco.puntosDefensa}")

print("------------------------------------------------------")
print(orco.puntosVida)
orco.puntosVida = 8
print(orco.puntosVida)

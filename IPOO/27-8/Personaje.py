class Personaje:
   
    #Constructor
    def __init__(self, nombre:str = "Personaje sin nombre", puntosVida:int = 10, puntosAtaque = 7, puntosDefensa:int = 5):
        self.nombre = nombre
        self.__puntosVida = puntosVida  #Con el __ Determinamos que el atributo es PRIVADO - Debemos usar el getter para obtener el valor
        self.puntosAtaque = puntosAtaque
        self.puntosDefensa = puntosDefensa
        print("Personaje creado correctamente")
        
    # getters y setters
    def getPuntosVida(self) -> int:
        return self.__puntosVida
    
    def setPuntosVida(self, puntosVida:int) -> None:
        if puntosVida > 0:
            self.__puntosVida = puntosVida

        
#Probando el constructor y el get y set para llamar un atributo privado

orco = Personaje()
print(f"Nombre: {orco.nombre}, Puntos de vida: {orco.getPuntosVida()}, Puntos de ataque: {orco.puntosAtaque}, Puntos de defensa: {orco.puntosDefensa}")

print("------------------------------------------------------")
print(orco.getPuntosVida())
orco.setPuntosVida(8)
print(orco.getPuntosVida())

print("------------------------------------------------------")
orco2 = Personaje("Pepito")
print(f"Nombre: {orco2.nombre}, Puntos de vida: {orco2.getPuntosVida()}, Puntos de ataque: {orco2.puntosAtaque}, Puntos de defensa: {orco2.puntosDefensa}")


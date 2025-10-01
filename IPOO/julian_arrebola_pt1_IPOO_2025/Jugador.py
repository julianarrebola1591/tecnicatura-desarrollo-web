import csv
from Equipo import Equipo
from Equipo import listaEquipos

def importarCsvJugador(ruta):
    with open(ruta, newline="", encoding="utf-8") as file:
        lista = []
        jugadoresCSV = csv.reader(file)
        for fila in jugadoresCSV:
            jugador = Jugador(int(fila[4]), str(fila[0]), str(fila[1]), float(fila[3]), str(fila[2]), int(fila[5]))
            lista.append(jugador)
        return lista
    

    
#Debo intentar utilizar la clase para guardar la lista de jugadores y de equipos
#Como puedo exportar lois datos a distintos archivos

class Jugador:
    def __init__(self, dni:int, nombreCompleto:str, fechaNacimiento:str, altura:float, equipo:str, puntosTotales:int):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.fechaNacimiento = fechaNacimiento
        self.altura = altura
        self.equipo = equipo
        self.puntosTotales = puntosTotales


def jugadoresMasAltos(listaJugadores:list) -> list:
    jugadorMasAlto = sorted(listaJugadores, key=lambda jugador : float(jugador.altura), reverse=True)[0]
    return jugadorMasAlto


def jugadoresConMasPuntos(listaJugadores):
    jugadorMasPuntos = sorted(listaJugadores, key=lambda jugador : int(jugador.puntosTotales), reverse=True)[:10]
    return jugadorMasPuntos
    
def alturaPromedio():
    #Realizar una lista de la altura promedio de los jugadores por cada equipo
    #Deberia primero descartar los equipos que no tengan ningun jugador
    #Si el equipo no está cargado en equipo.csv, pero si está en el jugador, debería contar?
    #Ejemplo: Rudy Gobert,1992-06-26,Minneapolis Timberwolves
    #Luego sacar el promedio de los que quedaron
    pass

              
print(" Gestion de jugadores y Equipos")
print("- - - - - - - - - - - - - - - - - - - - - - - - -")

listaJugadores = importarCsvJugador("2025-TR-jugadores.csv")
print(f"El jugador mas alto es: {jugadoresMasAltos(listaJugadores).nombreCompleto}")
print("")

print("- - - - - - - - - - - - - - - - - - - - - - - - -")
print("Lista de los 10 jugadores con mas puntos")
print("")
for jugador in jugadoresConMasPuntos(listaJugadores):
    print(f"{jugador.nombreCompleto}  -  {jugador.puntosTotales}")


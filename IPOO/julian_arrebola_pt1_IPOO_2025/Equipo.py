import csv

def importarCsv(ruta):
    with open(ruta, newline="", encoding="utf-8") as file:
        lista = []
        jugadores = csv.reader(file)
        for fila in jugadores:
            equipo = Equipo(str(fila[0]), str(fila[1]), int(fila[2]), int(fila[3]))
            lista.append(equipo)
        return lista
    
    
class Equipo:
    def __init__(self, nombre:str, ciudad:str, partidosJugados:int, partidosGanados:int):
        self.nombre = nombre
        self.ciudad = ciudad
        self.partidosJugados = partidosJugados
        self.partidosGanados = partidosGanados
        
        
def equiposMasGanadores(listaEquipos) -> list:
    #Ordenar los equipos de mayor a menor
    #EquimosOrdenados = sorted(listaEquipos, key=lambda equipo : int(equipo.partidosGanados) , reverse=True)
    listaGanadores = []
    maxGanados = max(equipo.partidosGanados for equipo in listaEquipos)
    for equipo in listaEquipos :
        if equipo.partidosGanados == maxGanados:
            listaGanadores.append(equipo)
    return listaGanadores
        
print(" Gestion de jugadores y Equipos")
print("- - - - - - - - - - - - - - - - - - - - - - - - -")
print("")


listaEquipos = importarCsv("2025-TR-equipos.csv")
EquiposGanadores = equiposMasGanadores(listaEquipos)
for equipo in EquiposGanadores:
    print(f"{equipo.nombre} - {equipo.partidosGanados}")

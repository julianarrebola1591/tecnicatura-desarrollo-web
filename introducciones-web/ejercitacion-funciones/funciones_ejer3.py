import math

#Modulos

def menuElegirForma():
    print("De que forma desea calcular el area?")
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo")
    print("4. Rombo")
    eleccion = int(input("Ingrese la opcion seleccionada"))
    return eleccion

def calcularRectangulo():
    medidaLado1 = int(input("Ingrese uno de los lados del rectangulo: "))
    medidaLado2 = int(input("Ingrese la medida del otro lado del rectangulo: "))
    areaRectangulo = int(medidaLado1*medidaLado2)
    return areaRectangulo

def calcularCirculo():
    medidaRadio = int(input("Ingrese el radio del circulo: "))
    areaCirculo = float(math.pi*medidaRadio*2)
    return areaCirculo

def calcularTriangulo():
    medidaAltura = int(input("Inrgese la altura del triangulo: "))
    medidaBase =  int(input("Ingrese la base del triangulo: "))
    areaTriangulo = float((medidaBase*medidaAltura)/2)
    return areaTriangulo

def calcularRombo():
    medidaDiagonalMayor = int(input("Ingrese la diagonal mayor del rombo del rombo"))
    medidaDiagonalMenor = int(input("Ingrese la diagonal menor del rombo del rombo"))
    areaRombo = float((medidaDiagonalMayor*medidaDiagonalMenor)/2)
    return areaRombo


#Main

eleccion = (menuElegirForma())

if eleccion == 1:
    print(calcularRectangulo())
if eleccion == 2:
    print(calcularCirculo())
if eleccion == 3:
    print(calcularTriangulo())
if eleccion == 4:
    print(calcularRombo())

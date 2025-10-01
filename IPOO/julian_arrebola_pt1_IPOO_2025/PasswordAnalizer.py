def leerTxt(ruta):
    with open ( ruta ) as txtClaves:
        lista = []
        for fila in txtClaves:
            lista.append(fila.strip())
        return lista

class PasswordAnalizer:
    def __init__(self, numeros:int = 2, mayusculas:int = 2, longitudMinima:int = 8):
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.longitudMinima = longitudMinima
    
    def esClaveFuerte (self, clave:str) -> str:
        cantNumeros = 0
        cantMayus = 0
        for caracter in clave:
            if caracter.isdigit():
                cantNumeros += 1
            elif caracter.isupper():
                cantMayus += 1
        
        if len(clave) >= self.longitudMinima and cantNumeros >= self.numeros and cantMayus >= self.mayusculas:
            return True
        else:
            return False
        
    def generarClave():
        pass
        
    def analizarClaves(self):
        lista = []
        clavesDebiles = leerTxt("claves.txt")
        for clave in clavesDebiles:
            if self.esClaveFuerte(clave) ==  False:
                lista.append(clave)
        return lista
        

        
analizar = PasswordAnalizer()
        
#Prueba de contraseña no fuerte
print(analizar.esClaveFuerte("Hola"))

#Prueba cumpliendo con mayus
print(analizar.esClaveFuerte("HolaPruebA"))

#Prueba cumpliendo con numeros y logitud
print(analizar.esClaveFuerte("Holaueba1233"))

#Prueba de contraseña fuerte
print(analizar.esClaveFuerte("HolaPRueba1233"))


regla1 = PasswordAnalizer(3, 1, 6)

print("----------------------------------")
print("A continuacion se ve la primer lista de claves debiles")

for clave in regla1.analizarClaves():
    print (clave)

regla2 = PasswordAnalizer(4, 3, 12)

print("----------------------------------")
print("A continuacion se ve la segunda lista de claves debiles")

for clave in regla2.analizarClaves():
    print (clave)

def potencia(base, exponente):
    resultado = base
    for i in range(exponente - 1):
        resultado = resultado * base
    return resultado

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(potencia(base,exponente))
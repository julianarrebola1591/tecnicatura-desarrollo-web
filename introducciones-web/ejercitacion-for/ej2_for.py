def suma_hasta(n):
    total = int(0)
    for i in range(n+1):
        total = total + i
    return total

#Main

numero_hasta = int(input("Ingrese hasta que numero quiere sumar: "))

print(suma_hasta(numero_hasta))
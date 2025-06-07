def factorialConFor(num):
    total = int(1)
    for i in range(num):
        total = total * (i + 1)
    return total

def factorialConWhile(num):
    i = 0
    total = int(1)
    while i < num:
        i = i + 1
        total = total * i
    return total

#MAIN

numeroFor = int(input("Ingrese un numero para que se calcule el factorial con FOR: "))
numeroWhile = int(input("Ingrese un numero para que se calcule el factorial con WHILE: "))


print(factorialConFor(numeroFor))
print(factorialConWhile(numeroWhile))

def determinarNumPrimo(num):
    contador = num - 1
    while 1 < contador:
        if (num % contador) == 0:
            return False
        contador -= 1
    return True


print(determinarNumPrimo(7))
num = int(input("Ingrese un numero: "))

def clasificarNumero(num):
    if num == 0:
        return print(f"el numero {num} es neutro")
    if num > 0:
        return print(f"el numero {num} es positivo")
    if num < 0:
        return print(f"el numero {num} es negativo")
    
#Main

clasificarNumero(num)
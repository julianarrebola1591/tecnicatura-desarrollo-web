def mayor_numero (num1, num2):
    if (num1 > num2):
        print(num1)
    else:
        print(num2)

#Main

print("Ingrese 2 numeros para saber cual es el mayor")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

mayor_numero(num1, num2)
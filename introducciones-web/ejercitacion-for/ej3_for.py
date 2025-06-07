def tabla_del(numero):
    for i in range(1,10):
        print(f"{numero} X {i} = {i * numero}")

#Main

num = int(input("Ingrese un numero del 1 al 9 para conocer su tabla de la multiplicacion: "))
if num < 10 and num > 0:
    tabla_del(num)
else:
    print("Debe ingresar un numero del 1 al 9")

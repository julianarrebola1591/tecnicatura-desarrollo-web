def procesarMontos ():
    monto = float(input("Ingrese el monto de la compra: "))
    montoTotal = monto
    while monto != 0:
        monto = float(input("Ingrese el monto de la compra: "))
        if monto >= 0:
            montoTotal += monto
        else:
            print("Ingrese un monto positivo")
    if montoTotal >= 1000:
        return montoTotal * 0.90
    return montoTotal

#MAIN

print(procesarMontos())
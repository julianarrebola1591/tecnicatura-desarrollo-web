total = float(input("Ingrese el total de la cuenta: "))

porcentaje_propina = int(input("Que porcentaje de propina quiere dar: "))

def calcular_propina (total, porcentaje_propina):
    monto_propina = float(total*porcentaje_propina/100)
    return monto_propina

#Main

print(calcular_propina(total, porcentaje_propina))
'''5) Crea un programa con tres funciones:
•	calcular_imc(peso, altura) que reciba el peso (en kg) y la altura (en metros) y devuelva el índice de masa corporal (IMC).
•	interpretar_imc(imc) que reciba el IMC y devuelva una clasificación:
•	Menor a 18.5 → "Bajo peso"
•	Entre 18.5 y 24.9 → "Normal"
•	Entre 25.0 y 29.9 → "Sobrepeso"
•	30.0 o más → "Obesidad"
•	diagnostico(peso, altura) que combine las dos funciones anteriores para devolver directamente el diagnóstico según peso y altura.'''

#Funciones

def calcular_imc(peso, altura):
    imc = peso / altura**2
    return imc

def interpretar_imc (imc):
    if (imc < 18.5):
        return "Bajo peso"
    elif (imc <= 24.9):
        return "Peso normal"
    else:
        return "Obesidad"

def diagnostico(peso, altura):
    
    imc = calcular_imc(peso, altura)
    return interpretar_imc(imc)

#Main
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))
print("todo en una funcion:")
##print(diagnostico(peso, altura))

prueba = int(10)
print(prueba)
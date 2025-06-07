def clasificar_edad (edad):
    if (edad < 13):
        print("Niño")
    elif (edad <= 17):
        print("Adolescente")
    else:
        print("Adulto")
    
#Main

edad = int(input("Ingrese su edad: "))

clasificar_edad(edad)
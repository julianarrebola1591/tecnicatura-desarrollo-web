def contar_letras(palabra, letra):
    contador = 0
    for i in palabra.upper():
        if i == letra.upper():
            contador = contador + 1
    print(contador)
    

palabra = str(input("Ingrese una palabra: "))
letra = str(input("Ingrese una letra: "))

contar_letras(palabra,letra)
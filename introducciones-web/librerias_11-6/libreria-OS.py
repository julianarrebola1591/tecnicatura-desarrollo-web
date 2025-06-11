import os

# Obtener el directorio actual
directorio_actual = os.getcwd()
print("Directorio actual:", directorio_actual)

# Cambiar al directorio de documentos
os.chdir("librerias-OS.py")

# Obtener el nuevo directorio actual
nuevo_directorio_actual = os.getcwd()
print("Nuevo directorio actual:", nuevo_directorio_actual)

import os

directorio_actual = os.getcwd()
print("Directorio actual:", directorio_actual)

os.chdir("C:/Users/WinyP/Documents")

nuevo_directorio_actual = os.getcwd()
print("Nuevo directorio actual:", nuevo_directorio_actual)

os.listdir()
import os
import time
import shutil
import msvcrt
import random

#Funciones-----------------------------------------------

def quit():
    if msvcrt.kbhit():
        tecla = msvcrt.getch().decode('utf-8').lower()
        if tecla == 'q':
            return True
    return False

def obtenerDir(ruta):
    if os.path.exists(ruta):
        os.chdir(ruta)
        return True
    else:
        print("No existe la carpeta!")

def renombrar(archivo):
        prefijo = random.randint(1000,9999)
        nuevoNombre = (f"{prefijo}_" + archivo)
        os.rename(archivo, nuevoNombre)
        return nuevoNombre

def envia(nombreArchivo, carpetaDestino):
    if os.path.exists(f'{carpetaDestino}\\{nombreArchivo}'):
        shutil.move(renombrar(nombreArchivo),carpetaDestino)
    else:
        shutil.move(nombreArchivo,carpetaDestino)

def clasificar(archivos,ruta):
    for archivo in archivos:

        #Musica
        if archivo[-4:] == ".mp3" or archivo[-4:] == ".wav" or archivo[-5:] == ".flac":
            carpetaMusica = os.path.join(ruta, 'Musica')

            if not os.path.exists(carpetaMusica):
                os.mkdir("Musica")

            envia(archivo,carpetaMusica)
        
        #Videos
        if archivo[-4:] in [".mp4", ".avi", ".mov", ".mkv"]:
            carpetaVideos = os.path.join(ruta, 'Videos')

            if not os.path.exists(carpetaVideos):
                os.mkdir("Videos")

            envia(archivo,carpetaVideos)

        #Imagenes
        if archivo[-4:] in [".jpg", ".png", ".gif"] or archivo[-5:] == "jpeg":
            carpetaImagenes = os.path.join(ruta, 'Imagenes')

            if not os.path.exists(carpetaImagenes):
                os.mkdir("Imagenes")

            envia(archivo,carpetaImagenes)

        #Documentos
        if archivo[-4:] in [".pdf", ".txt", ".doc", ".xls"] or archivo[-5:] in [".docx", ".xlsx"]:
            carpetaDocs = os.path.join(ruta, 'Documentos')

            if not os.path.exists(carpetaDocs):
                os.mkdir("Documentos")
            
            envia(archivo,carpetaDocs)

#Programa

print("ruta actual:", os.getcwd())
dir = input ("Ingresa ruta de Carpeta a clasificar: ")

count=0

while obtenerDir(dir):

    clasificar(os.listdir(),dir)

    print('''
          
          Clasificando archivos!
          Presione tecla 'q' para finalizar!

          ''')


    if quit():
        break

    time.sleep(5)

import csv
from importlib.resources import path
import os
import errno
import shutil

#Inicializando Variables
initial_count = 0
completados = 0
archivosExistentes = 0
contador = 0
contenido = []

#Folder Path
path = r"C:\Users\OSP2021\Documents\Organizador_Archivos\Pruebas_epud"
autorPath = r"C:\Users\OSP2021\Documents\Organizador_Archivos\Pruebas_epud\Organizacion"

#Change the directory
os.chdir(path)

#Realiza el conteo de cuantos archivos del tipo a exportar se encuentran en la carpeta.
for file in os.listdir():
    if os.path.isfile(os.path.join(path, file)) and file.endswith(".epub"):
        initial_count += 1
    #endif
#endfor

#Archivo EPUB File
def archivo_EPUB_file(file_path, file, autorPath):
    nombre = str(file)
    datoRepetido = nombre.find("(")
    if(datoRepetido == -1):
        desde = nombre.find("-")
        nombreNew = nombre[:desde-1]
        hasta = nombre.find("epub")
        autor = nombre[desde+2:hasta-1]
        nombre = nombreNew
    else:
        nombreNew = f'{nombre[:datoRepetido-1]}.epub'
        desde = nombreNew.find("-")
        hasta = nombreNew.find("epub")
        autor = nombreNew[desde+2:hasta-1]
        nombre = nombreNew[:desde-1]
    
    try:
        ruta = f'{autorPath}\{autor}'
        os.makedirs(ruta, exist_ok=False)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    source = file
    target = f'{autorPath}\{autor}\{nombre}.epub'
    
    global exito
    
    if(os.path.isfile(f'{target}')):
        print("el archivo existe, no se hace nada...")
        exito = False
        return(exito)
    else:
        #print(completados)
        shutil.copy2(file, target)
        exito = True
        return(exito)
    #shutil.copy2(file, target)
    #shutil.move(file, ruta)


#iterate through all file
for file in os.listdir():
    #Check whether file is in text format or not
    if file.endswith(".epub"):
        #contador += 1
        file_path = f"{path}\{file}"
        #call read text file funtion
        archivo_EPUB_file(file_path, file, autorPath)
        if(exito==True):
            completados += 1
        else:
            archivosExistentes += 1
        #time.sleep(2)
    #endif
#endfor
print(f"De los {initial_count} archivos precesados, \n Se han organizado {completados} archivos y \n se han encontrado {archivosExistentes} Archivos existentes")
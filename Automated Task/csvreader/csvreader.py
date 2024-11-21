#leer y procesar un archivo csv en python
import csv

#Abre el archivo 'receivers.csv' en modo lectura ('r')
with open('receivers.csv', 'r') as archivo:
    leer = csv.reader(archivo) # Lee el archivo CSV utilizando el lector CSV de Python
    #next(leer) # si queremos saltar la primera fila

    for fila in leer: #itera sobre cada fila, extrayendo los datos.
        print(' - '.join(fila)) #imprime las filas separandolas con el guion[ - ]
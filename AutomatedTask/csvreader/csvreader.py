#leer y procesar un archivo csv en python
import csv

#Abre el archivo 'receivers.csv' en modo lectura ('r')
with open('receivers.csv', 'r') as csv_file:
    read = csv.reader(csv_file) # Lee el archivo CSV utilizando el lector CSV de Python
    #next(read) # si queremos saltar la primera fila

    for row in read: #itera sobre cada fila, extrayendo los datos.
        print(' - '.join(row)) #imprime las filas separandolas con el guion[ - ]
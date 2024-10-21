"""
Confeccione un programa en Python que lea los datos generales del cliente
y luego busque dentro de los datos cargados si se encuentra la palabra : "Celular"   y
la palabra "Correo",   Si efectivamente se encuentra alguna de esas 
palabras debe imprimir los valores con esa información:  
Utilice la operación de Extracción de cadenas
"""
datosdelcleinte = input('Coloque los datos del cliente: ')
palabra_1 = input('Coloque la 1era palabra a buscar: ')
palabra_2 = input('Coloque la 1era palabra a buscar: ')

if datosdelcleinte.find(palabra_1) and datosdelcleinte.find(palabra_2) >=0 :
    print(f'\n Las palabras "{palabra_1}" y "{palabra_2}" fueron encontradas en los datos del cliente')
else:
    print(f'\n Las palabras no fueron encontradas')
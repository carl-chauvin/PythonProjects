'''
Escriba un programa que cargue una lista a partir de 5 nombres que se le solicitaran al usuario desde pantalla.
Luego se le solicitara al usuario que coloque un texto o cadena a buscar.  
Se debe recorrer la lista de nombres y buscar cuantas veces se encuentra el texto indicado en la lista.
'''

def BusquedaTexto():
    lista = []

    print(f'Ingrese 5 nombres a lista')

    for texto in range(5):
        NombreComp = input(f'Nombre {texto + 1}: ')
        lista.append(NombreComp)

    palabra = input(f'Introduzca el texto a buscar: ')
    
    contador = 0

    for nombre in lista:
        if palabra.lower() in nombre.lower():
            contador += 1
    
    return f'El texto {palabra} fue encontrado {contador} en la lista.'

print(BusquedaTexto())
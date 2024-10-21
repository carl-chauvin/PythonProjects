"""
Para practicar los métodos de las listas se solicita crear un programa en Python 
que cargue una lista de 5 elementos de cualquier tipo. 
Luego esa lista debe enviarse como argumento a una función llamada "PresentarLista".  
Dicha función utilizara varios métodos para realizar las siguientes operaciones en la lista:

Presentar la lista original
Presentar la lista invertida
Presentar la lista ordenada
Remover el último elemento ingresado.
Presentar la lista final
Indicar la cantidad de elementos
"""


print('**Programa de Metodos de Listas **\n')

def elementos(lista):
    print(f'Lista original: {lista}')
    
    lista.reverse()
    print(f'Lista invertida: {lista}')
    
    print(f'Lista ordenada: {sorted(lista)}')
    
    del(lista[0]) #lista.remove([4]) Me sale un error cuando uso remove, use delete en su lugar.
    print(f'Lista despues de remover el ultimo elemento: {sorted(lista)}')
    
    print(f'Cantidad de elementos: {len(lista)}')

lista = [input(f'Ingrese el elemento {i+1}: ') for i in range(5)]


elementos(lista)


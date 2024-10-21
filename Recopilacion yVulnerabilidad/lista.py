# #Iteracion de listas
# # nombres = ['James', 'Carlos', 'Pierre']

# # for nombre in nombres:
# #     print(nombre, end=', ')


# #Recuperacion de elementos por indice
# # lista = [25, 30, 45, 58]
# # lista[0] = 49
# # lista[3] = 89
# # print(lista)

# #Preguntar si un valor existe en mi8 lista
# numeros = [200, 201, 202, 300, 301, 302]
# #numero_a_buscar = 202

# # if numero_a_buscar in numeros:
# #     print(f'Si existe {numero_a_buscar} en mi lista de numeros.')
# # else:
# #     print(f'No existe {numero_a_buscar} en mi lista.')

# #Recuperar el indice de cierto elementos
# # indice = numeros.index(numero_a_buscar)
# # print(f'El indice del numero {numero_a_buscar} es: {indice}')
# # valoresRecuperados = numeros[2:] #numeros = [0,3...2,4...1,5...]
# # print(f'Los valores cuperados de la lista son: {valoresRecuperados}')

# #Realizar una copia
# lista_copiada = numeros[:]
# # numeros[1] = 560
# # print(f'La lista original es: {numeros}')
# # print(f'La lista copiada es:{lista_copiada} ')

# # Metodos de listas
# largoLista = len(numeros)
# print(f'Largo lista: {largoLista}')

# # Agregar un nuevo elemento al final de la lista ".append()"
# numeros.append(800)
# print(f'La nueva lista es: {numeros}, se agrego el numero 800.')

# # Insertar nuevos elementos, en el indice deseado: NombreLista.insert(numeroIndice, elementoAgregado)
# numeros.insert(3, 900)
# print(f'Lista con el nuevo valor: {numeros}')

# # Eliminar un valor de una lista
# numeros.remove(900)
# print(numeros)

# # Eliminar un elemento por indice
# del numeros[5]
# print(numeros)

# #Eliminar la lista completa
# numeros[:] = []
# print(numeros)

# # Eliminar por completo la variable
# del largoLista 
# print(largoLista)


# print("*** Manejo de Tuplas ***")
name = ('carl', 'lunes', 'frutas')
# print(name)

# # Tuplas heterogenea
# tupla_heterogenea = ('nandy', 250, True)
# print(tupla_heterogenea)

# # Recorrer los elementos de una tupla
# for nombre in name:
#     print(nombre, end='-') #pass nos permite omitir el bloque de codigo del ciclo 'For'
#     #al momento de acceder al indice de una tupla se debe usar corchetes'[]'
#     #las tuplas no puede ser modificada, no se puede cambiar elementos de una tupla
#     pass
nom_nuevo = 'frutas'
if nom_nuevo in name:
    print(f'El nombre {nom_nuevo} si existe en la tupla')
else:
    print(f'El {nom_nuevo} no existe en la tupla.')
print('*** Manejo de Set en Python ***')
# Un set es un conjunto de datos no ordenados// No se pueden repetir sus elementos
datos = {'jimy', 500 , 500, 'nandy', 'carlos', 'john', 'nandy'}
#print(datos)
#No pueden modificar sus elementos

#Iteracion
for dato in datos:
    pass #para que no se ejecute el ciclo for
    print(dato, end=",\n")

elemento_disponible = 'john'

if elemento_disponible in datos:
    print(f'El elemento {elemento_disponible} si existe en la variable Datos.')
else:
    print(f'El elemento {elemento_disponible} no se encuentra disponible en la variable Datos.')

largo = len(datos)
print(f'La cantidad de elementos en la variable Datos es:{largo}')

#eliminar elementos
datos.remove(500)
print(datos)

#agregar un nuevo elemento
datos.add('Chauvin')
print(datos)


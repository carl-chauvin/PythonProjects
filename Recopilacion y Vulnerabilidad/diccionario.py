print('*** Manejo de Diccionarios en Python ***')
# Este proceso define la forma de trabajar con 
# una operacion CRUD(Create - Read - Update - Delete) en un Diccionario

datos = {
    'Nombre': 'David',
    'Apellido': 'Krasovic',
    'Edad': 35,
    'Profesion':'Fútbolista'
}
print(datos)

#acceder a los elementos
print(f"Nombre: {datos['Nombre']}")
print(f"Apellido: {datos['Apellido']}")
print(f"Edad: {datos.get('Edad')}")
print(f"Profesion: {datos.get('Profesion')}")

#Para saber el largo 
print(f"La cantidad de elemento del Diccionario es: {len(datos)}")

#Agregar nuevo elemento en un diccionario
datos['Equipo']='Barcelona'
datos['Pais']='Panamá'
print(datos)
print(f"Equipo: {datos.get('Equipo')}")
#Obtener una lista de las llaves del diccionario
print(f'Lista de las llaves del Dic. datos: {datos.keys()}')
#Obtener una lista de los valores del diccionario
print(f'Lista de los valores del Dic. datos: {datos.values()}')
#Obtener los elementos del diccionario(recupera los elementos en forma 
# de tupla de llave y valor asociado
print(f'Lista de los elementos del Dic. datos: {datos.items()}')
#Revisar si existe una llave en el diccionario
llave_nueva = 'Pais'

if llave_nueva in datos:
    print(f'la llave nueva {llave_nueva} si existe en el diccionario Datos')
else:
    print(f'la llave nueva {llave_nueva} no existe en el diccionario Datos')

#Actualizar(modificar) un elemento del diccionario
datos['Nombre']='Carl'
print(f'Nuevo nombre: {datos}')
#Eliminar un elemento del diccionario
datos.pop('Pais')
print(f'La llave "Pais" se ha eliminado, observe el resultado: {datos}')

#Recorrer las llaves del diccionario (keys)
for llaves in datos.keys():
    pass
    print(llaves, end=', ')
print()
#Recorrer las valores del diccionario (values)
for valores in datos.values():
    print(valores, end=', ')
print()
#Recorrer los elementos del diccionario en forma de tupla
for llaves, valores in datos.items():
    print(f'Llave: {llaves}, Valor: {valores}')

#Eliminar todos los datos del diccionario
datos.clear()
print(f'El Diccionario Datos no tiene elementos: {datos}')


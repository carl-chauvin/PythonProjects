print('*** Listas y Diccionarios ***')
#Listas y Diccionarios
Personas = [
    {
        'Nombre':'Roger',
        'Apellido':'Kravic',
        'Edad':'31'
    },
    {
        'Nombre':'James',
        'Apellido':'Rodriguez',
        'Edad':'29'
    },
    {
        'Nombre':'John',
        'Apellido':'Smith',
        'Edad':'35'
    }
]
print(f'Tenemos 2 personas con las siguientes informaciones: {Personas}')

#Para imprimir el primer valor
print(Personas[0])
print(Personas[1])
print(Personas[2])
print()
#Acceder a un valor (llave[keys]) nombre del primer diccionario
print(Personas[0].get('Nombre'))
print()

#Recorrer los elementos de la lista (elemento = diccionario) 
# usamos la funcion 'enumarate' para enumerar cada uno de 
# los elementos que tenemos en la lista
# [Imprime los diccionarios por separados y con sus indices]
for conteo, persona in enumerate(Personas):
    print(f'Persona: {conteo}: {persona}')
print()
#para sacar solo el nombre de los diccionarios
for conteo, persona in enumerate(Personas):
    print(f'Persona: {conteo}: {persona.get('Nombre')}')
"""
Para practicar algunas de las operaciones con cadenas de caracteres, 
se solicita que confeccione un programa en Python que Lea desde el teclado 
una Cadena de texto y luego solicite una 2da cadena mas pequeña (sub-cadena) 
, la cual será buscada en la primera cadena.   Si la sub-cadena es encontrada 
debe indicar: ¿En que posición encontró la sub-cadena?.   Utilice el Método find.
"""

cadena = input('Coloque los datos de la cadena 1: ')
subcadena = input('Coloque los datos de la sub-cadena: ')

posición = cadena.find(subcadena)

print(f'\n La sub-cadena fue encontrada en la posición: {posición}')
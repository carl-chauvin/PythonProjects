"""
Se solicita que confeccione un programa en Python que utilice el 
ciclo de repetición while para sumar 3 números impares  

Utilizando la sentencia continue debe saltar los números pares que el usuario introduzca. 
El ciclo debe acabar cuando se ingrese el tercer numero impar.
"""

lista = [ ]

impar_num = 0

print(f'**Programa de conteo de Numeros Impares**')

while impar_num < 3:
    numero = int(input(f'Ingrese un numero: '))
    if numero % 2 == 0:
        continue
    lista.append(numero)
    impar_num +=1


print(f'La suma de los 3 numeros impares es:{sum(lista)}')
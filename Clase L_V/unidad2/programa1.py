"""
Se solicita que confeccione un programa en Python que cargue una lista de 7 notas.

Luego debe recorrer la lista con un FOR para obtener el promedio de las notas
y finalmente debe indicarle al usuario cual es su nota literal :

A = Promedio mayor o igual a 91;
B= Promedio entre 81 y 90;
C= Promedio entre 71 y 80:
D= promedio entre 61 y 70;
E= Promedio menor a 61
"""
lista = [ ]
suma = 0
print(f'**Programa de Ingresos de Notas**')

for i in range(7):
    nota = int(input(f'ingrese sus nota: '))
    lista.insert(i, nota)
    suma = suma + lista[i]
    promedio = suma/7
print(f'Promedio de notas: {promedio:.2f}')
if promedio >= 91:
    print(f'Usted obtuvo una A')
elif 81 <= promedio < 91:
    print(f'Usted obtuvo una B')
elif 71 <= promedio < 81:
    print(f'Usted obtuvo una C')
elif 61 <= promedio < 71:
    print(f'Usted obtuvo una D')
else:
    print(f'Usted obtuvo una F')
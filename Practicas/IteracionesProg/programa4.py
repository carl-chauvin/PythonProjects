#Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input('Ingresar un numero entro positivo: '))

for i in range(num, -1, -1):
    print(i, end=',')
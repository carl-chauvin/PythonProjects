""" Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es un número primo o no. """

num = int(input("Ingrese un numero entero en pantalla: "))
i = 2

while num % i != 0:
    i+=1
if num == i:
    print(f"{num} es un numero primo")
else:
    print(f"{num} no es un numero primo")

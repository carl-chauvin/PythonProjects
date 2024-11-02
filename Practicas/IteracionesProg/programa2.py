#Escribir un programa que pregunte al usuario su edad y muestre por pantalla
#  todos los años que ha cumplido (desde 1[el primer año] hasta su edad).

edad = int(input('Introduzca tu edad: ')) #usamos int e input para que el usuario pueda ingresar su edad

for i in range(edad): # iteramos en i usando la funcion "range" para que nos imprima las edades desde 1 hasta el final
    suma = str(i+1) # declaré la variable *suma para sumar las edades de 1 en 1 hasta llegar a la edad ingresada
    print('Has cumplido',suma,'año(s)') # el resultado en pantalla con "print"

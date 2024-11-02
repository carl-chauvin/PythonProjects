""" Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. """

for i in range(1, 11): #Primero declaramos interamos I
    for j in range(1, 11): #despues creamos una nueva iteracion J para hacer la mult
        print(i*j, end='\t') #end='\t' nos da el resulta en forma de table
print('') # para el almacenar el resultado final
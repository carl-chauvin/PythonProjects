#Generador de ID

#importar random value para generar un valor aleatorio
from random import randint

#Imprimir nombre del sistema
print("***Sistema de Generador de ID Unico*** \n")

#Declaramos las variables
nombre = input("Cual es tu Nombre?: ")
apellido = input("Cual es tu Apellido?: ")
fecha_nac = input("Cual es tu Año de Nacimiento?: ")
valor_al = randint(0, 9999)

#Imprimir el resultado final
print("Hola " + nombre , ", habitante de Cuidad de Panamá \n Tu numero de indentificación (ID) generado por el sistema es: \n"
,nombre[0:2].upper() + apellido[0:2].upper() + fecha_nac[2:4] + str(valor_al)
   ,"\n\nFelicidades!" )

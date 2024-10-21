print('*** Funciones en Python ***')

#Definir una funcion simple
def nuevo():
    print('Hello Mundo, este es un ejemplo de una funcion.')
#Llamar a la funcion

nuevo()

#Ejemplo #2 de una funcion
def nuevo(parametro):
    print(f'Mensaje del sistema: {parametro}')
print()
#Llamar a la funcion
argumento = input('Escribe lo que quieres: ') #'Llamar a una funcion con un parametro y un argumento.'
nuevo(argumento)
# Pasar una nueva cadena a una funcion(mensaje aparece directamente cuando la llamamos)
# nuevo('Mensaje nuevo.')
#----------------------------------------
def suma(a=0, b=0, c=0):
    print(a + b + c)

# Fin 
suma(10, 5, 2)
suma(3)
suma(9, 4)
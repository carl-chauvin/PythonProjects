"""
album_year = 1983
album_year = 1990

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

_____________________________________________________________________
#Revisar si un numero es positivo

print("***Revision de numero positivo***")

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print(f'el numero {numero} es Positivo')
elif numero < 0:
    print(f'el numero {numero} es Negativo')
else:
    print("El numero ingresado es cero(0)")
____________________________________________________________________

i = 1
while i < 6:
    print(i)
    i += 1 # i = i + 1 //+= es un operador de asignacion compuesto
 """
# Menu Interactivo con el ciclo While.

print('*** Sistema de Administracion de Cuentas ***')

salir = False
while not salir:
    print(f'''
         Menu:
             1. Crear cuenta.
             2. Eliminar cuenta.
             3. Salir.
''')

    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
            print('Su cuenta fue creada correctamente...')
    elif opcion == 2:
            print('Su cuenta fue Elininada ....')
    elif opcion == 3:
            print('Saliendo del sistema ....')
            salir = True
    else:
            print('Opcion invalida. Escoge numeros del 1 a 3.') 

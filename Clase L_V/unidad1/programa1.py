"""
Se solicita que confeccione un programa en Python que emule una calculadora. 
Para ello debe solicitar 2 valores desde el teclado y luego desplegar un menu 
con las posibles operaciones a realizar (1.Suma 2.Resta  3. Multiplicación 
4. División  5. Residuo).    El usuario debe indicar cual operacion quiere realizar 
y el  programa debe presentar el resultado final.
"""

print("**Calculadora en Python.**")



salir = False
while not salir:
    print("Indique que operacion desea realizar: ")
    print('''
    1. Suma
    2. Resta
    3. Multiplicación
    4. Division
    5. Residuo
    ''')
    opcion = int(input("Operación: \n"))

    if opcion == 1:
        valor1 = float(input("Coloca el valor 1: "))
        valor2 = float(input("Coloca el valor 2: "))
        suma = valor1 + valor1
        print(f'\n El total de la Suma es: {suma}\n')
    
    elif opcion == 2:
        valor1 = float(input("Coloca el valor 1: "))
        valor2 = float(input("Coloca el valor 2: "))
        resta = valor1 - valor1
        print(f'\n El total de la Resta es: {resta}\n')

    elif opcion == 3:
        valor1 = float(input("Coloca el valor 1: "))
        valor2 = float(input("Coloca el valor 2: "))
        multi = valor1 * valor1
        print(f'\n El total de la Multiplicación es: {multi}\n')

    elif opcion == 4:
        valor1 = float(input("Coloca el valor 1: "))
        valor2 = float(input("Coloca el valor 2: "))
        divi = valor1 / valor1
        print(f'\n El total de la División es: {divi}\n')

    elif opcion == 5:
        valor1 = float(input("Coloca el valor 1: "))
        valor2 = float(input("Coloca el valor 2: "))
        resid = valor1 % valor2
        print(f'\n El total del Residuo es: {resid}\n')

    else:
        salir = True
  
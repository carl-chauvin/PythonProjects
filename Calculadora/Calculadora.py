#Calculadora en Python

print("**Calculadora en Python.**")

print("**Operaciones que puedes realizar:**")

salir = False
while not salir:
    print('''
    1. Suma
    2. Resta
    3. Multiplicación
    4. Division
    5. Salir
    ''')
    opcion = int(input("Escoje una opcion: "))

    if opcion == 1:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        suma = valor1 + valor1
        print(f'\n El total de la Suma es: {suma}')
    
    elif opcion == 2:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        resta = valor1 - valor1
        print(f'\n El total de la Resta es: {resta}')

    elif opcion == 3:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        multi = valor1 * valor1
        print(f'\n El total de la Multiplicación es: {multi}')

    elif opcion == 4:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        divi = valor1 / valor1
        print(f'\n El total de la División es: {divi}')

    elif opcion == 5:
        print("Gracias por usar nuestra calculadora en linea. Saliendo del Sistema.")
        salir = True

    else:
        print("Opcion invalida. Elegir entre 1 a 5.")
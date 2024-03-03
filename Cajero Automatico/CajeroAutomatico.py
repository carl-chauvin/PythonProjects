#Programa de cajero automatico

print("*** Mi Cajero Automatico con Python ***")

#declaramos la variable con el saldo total en la cuenta bancaria
saldoDisponible = 2000
#con el ciclo while hacemos una iteracion para que el programa no se rompa hasta elegir la opcion 4
salir =  False
while not salir:
    print(f'''
    Operaciones que puedes realizar
    1. Consultar saldo.
    2. Retirar.
    3. Depositar.
    4. Salir.''')

#declaramos una variable para elegir una opcion
    opcion = int(input('Escoje una opcion: '))

#creamos la condicion para cada opcion disponible
    if opcion == 1:
        print(f'\n El saldo disponible es: B./{saldoDisponible}. \n')
    elif opcion == 2:
        mensaje = float(input('Ingresa el monto a retirar: '))
        #validacion1
        if mensaje <= saldoDisponible:
            saldoDisponible -= mensaje
            print(f' \n Has retirado {mensaje} y tu Saldo actual es: B./{saldoDisponible}.')
        else:
            print(f'No cuentas con saldo suficiente. Salfo actual {saldoDisponible}')
    elif opcion == 3:
        mensaje2 = float(input('Ingresa el monto a depositar: '))
        saldoDisponible += mensaje2
        print(f' \n Has depositado {mensaje2} y tu saldo actual es: B./{saldoDisponible}.')
    elif opcion == 4:
        print('Saliendo del sistema ... \n')
        salir = True
    else:
        print('Opcion invalida, elija entre 1 a 4.')
        

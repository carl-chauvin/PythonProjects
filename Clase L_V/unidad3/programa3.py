"""
Se solicita crear una función que convierta un número entero entre 1 y 1000 en el número literal (número en letras)
La función debe solicitar un argumento (número entero), y debe retornar un string con el número literal
"""
def NumeroALetras(n):
    if n < 1 or n > 1000:
        return "El número debe estar entre 1 y 1000"

    unidades = [" ", "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = {11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince"} #use un diccionario para poder identificar los numeros especiales
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if n == 1000:
        return "mil"
    
    literal = ""


    if n >= 100:
        literal += centenas[n // 100] + " "
        n %= 100

    
    if 11 <= n <= 15:
        literal += especiales[n]
    else:
        
        if n >= 10:
            if n % 10 == 0:  
                literal += decenas[n // 10]
            else:
                literal += decenas[n // 10] + " y "
            n %= 10

        
        literal += unidades[n]

    return literal.strip()


numero = int(input("Introduzca un numero enteri entre 0 y 1000: "))
print(f'El numero introducido en letras es: {NumeroALetras(numero)}')

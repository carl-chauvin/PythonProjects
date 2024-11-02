#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
#  y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#Declaracion de las variables
cantidadInvert = float(input('Cantidad a Invertir: '))
InteresAn = float(input('Interes Anual: '))
NumeroAn = int(input('Numero de Año: '))

for i in range(NumeroAn):
    suma = str(i+1) # hace el conteo de los años de 1 en 1
    cantidadInvert *= 1 + InteresAn / 100 #para calcular le interes anual y 
    #muestre el capital obtenido en la inversion
print(f'El capital en el año {suma} es {cantidadInvert:.2f}') #tambien se puede usar el metodo round
#para obetenr 2 numeros decimales al final ex: str(round(cantidadInvert, 2))

#El operador *= equivale a multiplicar una variable 
# por otra y almacenar el resultado en la primera, es decir x*=2 equivale a x=x*2 .

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
#los números impares desde 1 hasta ese número separados por comas.
num = int(input('Ingrese un numero entrero(impar) positivo: '))

for i in range(1,num+1,2): #empieza desde el primer numero ([start]1), sumara el numero ingresado ([stop]num+1) y los pasos[step] se heran de 2 en 2.
    #if i % 2 != 0: sirve si queremos ver los numeros impares sin llegar al numero ingresado
    print(i, end=',')

'''
if num % 2 == 0:
    print('ES correcto')
else:
    print('Incorrecto')
'''
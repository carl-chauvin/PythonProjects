#Generador de ID

#Imprimir nombre del sistema
print("***Bienvenido al Sistema de Generación de Emails de Hello Code*** \n")

#Declaramos las variables
nombre = input("Cual es tu Nombre?: ")
apellido = input("Cual es tu Apellido?: ")
domain = "@hellocode.com"

#email_generado = f'{nombre.lower()}.{apellido.lower()}@hellocode.com'=>  Impresión de interpolación.

print("Tu nuevo email generado por el sistema es: \n\n",
    nombre.lower() + "." + apellido.lower() + domain
    ,"\n\n ***Felicidades***"
)

"""
a = 28
b = 30

a /= b ; a *= b ; a -= b ; a += b
print(a)
"""
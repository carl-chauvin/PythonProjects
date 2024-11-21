"""  
#Modulo que se usa para obtener la hora actual
from time import *
print(asctime())

#para tener ayuda de cualquier modulo
print(help("math")) 
"""
# Ejercicios
from math import *
import math as mt
#1
""" 
x = 5
a = mt.tan(x**3)
print(a)
"""
#2
""" 
a = mt.cos(pi + 0.2)-3/mt.tan(sqrt(2)-2)+0.2**3
print(a)
"""
#3
""" 
x = 6
a = sqrt(2)+1/mt.sin(2)-0.1 + 2 / x**2 - 1
print(a)
"""
#4
""" 
b = 3
c = 2
y = not b < 5 or c == 0
print(y)
"""
#5
""" 
a = 5
b = 3
c = 2
z = not a < b or c == 5
print(z)
"""
#6
""" 
a = 5
b = 6
c = 8
t = (a + b + c)/2
s = sqrt(t*(t-a)*(t-b)*(t-c))
print(s)
#14.981238266578634
"""
#7 : calcular el area total de un bloque de dimensiones
""" a = 20
b = 30
c = 40
a_t = a * b * c
print(a_t) """

#8 calcular el area de un cilindro
""" r = 5
a = 4
ac = 2*pi*r*a+r
print(f"El area del Cilindro es: {ac}") """

#9 Calcular el area de un triangulo rectagulo
""" 
a = 5
b = 40
a_t = int(b*a/2)
print(f"El area total del triangulo rectangulo es: {a_t}")
"""
a = 13
b = 10**7
print(a*b)
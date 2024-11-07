"""
import sys
print (sys.version)

print("Hello, World")

carl = 'Michelle es un nombre personal'


print(carl.split())

for i in range(-5, 5):
   print(i)
"""
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
name = []
i = 0
while i <len(Animals):
    j = Animals[i]
    if len(j)==7:
        name.append(j)
    i = i + 1
print(name)
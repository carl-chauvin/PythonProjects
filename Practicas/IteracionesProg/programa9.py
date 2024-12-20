""" Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la contraseña 
hasta que introduzca la contraseña correcta. Se puede usar el ciclo While como el For
""" 
""" password = "pass5991"
text = " "
while password != text:
    text = input("Introduzca la contraseña: ")
print("contraseña incorrecta")
 """

password = "pass5991"

for i in password:
    variable = input("Introduzca la contraseña: ")
    if variable != password:
        print(f"La contraseña es incorrecta, vuelve mas tarde!")
        continue
    else:  
        print(f"Acertaste, la contraseña {variable} introducida es correcta.")
        break

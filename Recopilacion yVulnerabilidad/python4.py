#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista y la muestre por pantalla el mensaje 
#Yo estudio <asignatura>,donde <asignatura> es cada una de las asignaturas de la lista.

#asignatura = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
#for asignaturas in asignatura:
#    print('Yo estudio', asignaturas)

message = int(input('Input your age: '))

if message <= 9:
    print('You will have milk porridge for breakfast')
elif message >= 10 and message <=14:
    print('You will have a sandwich for breakfast')
elif message <=15 and message >=17:
    print('You will have a burger for breakfast')

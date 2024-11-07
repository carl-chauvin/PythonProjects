#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista y la muestre por pantalla.
"""
a_curso = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
print(a_curso)


A=(0,1,2,3,4,5,6,7)
print(A[2:7])

B=["a","b","c"]
print(B[1:])
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}

release_year_dict['chauvin'] = 1995
del(release_year_dict['chauvin'])

print(release_year_dict)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print(album_set1 & album_set2)
print(album_set1, album_set2)
print(album_set2.difference(album_set1))
print(album_set2.union(album_set1))

#There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. 
#They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.

Annie = 1997
Jane = 1999

if Annie%4 == 0:
    print('Annie were born in a leap year')
elif Jane%4 == 0:
    print('Jane were born in a leap year')
else:
    print('None of them was bron in a leap year')


def Equation(a,b):
    a=2
    b=3
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 
"""
def div(a,b):
    c = (a/b)
    return c

div(4, 2)

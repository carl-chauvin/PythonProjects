'''
nombre = '' #StringVar()
nombre.set('Me llamo Carl')
print('Repuesta: ',nombre.get())

#------------------------------------------------------------------------------------
from tkinter import * #Sirve para instalar todas las propiedades de la libreria

raiz = Tk() #creamos un obejto relacionado con la libreria
raiz.title('Ventana de Practica de Tkinter') # .title me proporciona el titulo de la ventana

miframe = Frame() #una variable tipo objeto, el metodo frame() me crea un cuadro en la ventana que estamos creando

miframe.pack(side='top') #le estoy diciendo que me ubique el cuadro en la parte de arriba
miframe.config(bg='gray') # .config me permite configurar algunas propiedades dentro de la ventana, mi background sera de color azul
miframe.config(width='500', height='300') #para configurar el largo y el ancho de la ventana

milabel = Label(miframe, text='Bienvenido a programacion con Tkinter')
milabel.place(x=40, y=25)

raiz.geometry('400x300') #para indicar el tamano de la ventana
raiz.mainloop() #Sirve para mantener la ventana fija 
#------------------------------------------------------------------------------------
'''
#Programa para calcular el precio del alquiler de vehiculos usando la libreria Tkinter
# --Tipo auto : Sedan         --> 35.00 por dia
# --Tipo auto : Sedan de Lujo --> 50.00 por dia
# --Tipo auto : Camionetas    --> 75.00 por dia

from tkinter import *
from tkinter import ttk #importamos esta libreria de tkinter para tener acceso al combobox

def obtenerTarifa():
    num = dias.get() #con el metodo .get() obtenemos la cantidad de dias
    tipovehiculo = valores.get() #con el metodo .get() obtenemos el tipo de vehiculo
    if tipovehiculo == '1. Sedan':
        tarifa = 35
    elif tipovehiculo == '2. Sedan de Lujo':
        tarifa = 50
    else:
        tarifa = 75
    total.set(str(tarifa * num)) #nos da el resultado final de la multiplicacion en formato de texto por el STR()[string]

ventana = Tk() #creamos un obejto relacionado con la libreria

ventana.title('Calculo de Alquileres de Autos') # .title me proporciona el titulo de la ventana

lblnombre = Label(ventana, text='Nombre Completo: ').place(x=20, y=30)
lbltipo = Label(ventana, text='Tipo del Vehiculo: ').place(x=20, y=60)
lblprecio = Label(ventana, text='Dias: ').place(x=20, y=90)


lbltarifa = Label(ventana, text='Tarifa Total: ').place(x=20, y=150)

entryNombre = Entry(ventana, width=30).place(x=150, y=30) #para el textbox de la entrada del texto

valores = StringVar() #la variable de control acumulara los valores seleccionado por el usuario
combo = ttk.Combobox(ventana, textvariable=valores, width=27, values=('1. Sedan', '2. Sedan de Lujo', '3. Camionetas')).place(x=150, y=60)
#dentro del copmbobox tenemos las opciones que el usuario puede elegir

dias = IntVar()
entryDias = Entry(ventana, textvariable=dias, width=17).place(x=150, y=90)

total = StringVar()
entryTotal = Entry(ventana, textvariable=total, width=17).place(x=150, y=150)

boton = Button(ventana, text='Calcular', command=obtenerTarifa, bg='darkgray').place(x=25, y=120)

ventana.geometry('400x300')
ventana.mainloop()
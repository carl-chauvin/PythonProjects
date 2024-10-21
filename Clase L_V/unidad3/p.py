'''
def d(x):
    v = x - 5
    r = x/x+1
    return r

z =-10
while True:

    r = d(z)
    print(r)

    z+=1

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


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Función para calcular la letra mensual del préstamo
def calcular_letra_mensual(monto_prestamo, tasa_interes, plazo_anos):
    tasa_mensual = tasa_interes / 12  # Convertir la tasa de interés a mensual
    num_pagos = plazo_anos * 12  # Convertir el plazo a meses
    cuota_mensual = monto_prestamo * (tasa_mensual / (1 - (1 + tasa_mensual)**(-num_pagos)))
    return cuota_mensual

# Función para calcular la prima mensual de la póliza de vida
def calcular_prima_vida(monto_prestamo, edad, genero, fumador):
    # Definir la tasa de vida según la edad y el género
    if genero == 'M':
        if 18 <= edad <= 40:
            tasa_vida = 0.003
        elif 41 <= edad <= 60:
            tasa_vida = 0.004
        else:
            tasa_vida = 0.006
    elif genero == 'F':
        if 18 <= edad <= 40:
            tasa_vida = 0.0025
        elif 41 <= edad <= 60:
            tasa_vida = 0.0035
        else:
            tasa_vida = 0.005
    
    # Si es fumador, aplicar un recargo del 50% a la tasa de vida
    if fumador == 'S':
        tasa_vida *= 1.5
    
    # Calcular la prima mensual
    prima_mensual = tasa_vida * monto_prestamo
    return prima_mensual

# Función para obtener los datos del formulario y realizar los cálculos
def cotizar_prestamo():
    try:
        nombre = nombre_entry.get()
        edad = int(edad_entry.get())
        genero = genero_entry.get().upper()
        fumador = fumador_entry.get().upper()
        tipo_prestamo = int(tipo_prestamo_entry.get())
        monto_prestamo = float(monto_prestamo_entry.get())
        plazo_anos = int(plazo_entry.get())

        # Asignar la tasa de interés según el tipo de préstamo
        if tipo_prestamo == 1:
            tasa_interes = 0.06  # Hipotecario
        elif tipo_prestamo == 2:
            tasa_interes = 0.13  # Personal
        elif tipo_prestamo == 3:
            tasa_interes = 0.09  # Automóvil
        else:
            messagebox.showerror("Error", "Tipo de préstamo inválido.")
            return

        # Calcular la letra mensual del préstamo
        letra_mensual = calcular_letra_mensual(monto_prestamo, tasa_interes, plazo_anos)

        # Calcular la prima mensual de la póliza de vida
        prima_mensual = calcular_prima_vida(monto_prestamo, edad, genero, fumador)

        # Mostrar los resultados
        result_text.set(f"Letra Mensual: {letra_mensual:.2f}\nPrima de Póliza de Vida: {prima_mensual:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese todos los datos correctamente.")

# Crear la ventana principal
root = Tk()
root.title("Cotización de Préstamos")
root.geometry("400x400")

# Crear las etiquetas y campos de entrada para los datos del cliente
Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
nombre_entry = ttk.Entry(root)
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Edad:").grid(row=1, column=0, padx=10, pady=10)
edad_entry = ttk.Entry(root)
edad_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Género (M/F):").grid(row=2, column=0, padx=10, pady=10)
genero_entry = ttk.Entry(root)
genero_entry.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Fumador (S/N):").grid(row=3, column=0, padx=10, pady=10)
fumador_entry = ttk.Entry(root)
fumador_entry.grid(row=3, column=1, padx=10, pady=10)

Label(root, text="Tipo de Préstamo (1. Hipotecario 2. Personal 3. Auto):").grid(row=4, column=0, padx=10, pady=10)
tipo_prestamo_entry = ttk.Entry(root)
tipo_prestamo_entry.grid(row=4, column=1, padx=10, pady=10)

Label(root, text="Monto de Préstamo:").grid(row=5, column=0, padx=10, pady=10)
monto_prestamo_entry = ttk.Entry(root)
monto_prestamo_entry.grid(row=5, column=1, padx=10, pady=10)

Label(root, text="Plazo (en años):").grid(row=6, column=0, padx=10, pady=10)
plazo_entry = ttk.Entry(root)
plazo_entry.grid(row=6, column=1, padx=10, pady=10)

# Crear el botón para calcular y mostrar los resultados
ttk.Button(root, text="Calcular", command=cotizar_prestamo).grid(row=7, column=0, columnspan=2, pady=20)

# Crear una etiqueta para mostrar los resultados
result_text = StringVar()
result_label = Label(root, textvariable=result_text, font=("Arial", 12))
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()

'''
from tkinter import *
from tkinter import ttk

# Función para calcular la letra mensual del préstamo
def obtenerLM(monto_prestamo, tasa_interes, plazo_anual):
    tasa_mensual = tasa_interes / 12
    num_pagos = plazo_anual * 12
    cuota_mensual = monto_prestamo * (tasa_mensual / (1 - (1 + tasa_mensual)**(-num_pagos)))
    return cuota_mensual

# Función para calcular la prima de vida
def obtenerPrimaVida(monto_prestamo, edad, genero, condicion):
    if genero == 'M':
        if 18 <= edad <= 40:
            tasa_vida = 0.003
        elif 41 <= edad <= 60:
            tasa_vida = 0.004
        else:
            tasa_vida = 0.006
    elif genero == 'F':
        if 18 <= edad <= 40:
            tasa_vida = 0.0025
        elif 41 <= edad <= 60:
            tasa_vida = 0.0035
        else:
            tasa_vida = 0.005
    
    if condicion == 'S':
        tasa_vida *= 1.5

    prima_mensual = tasa_vida * monto_prestamo
    return prima_mensual

# Función para manejar la lógica de cálculo del préstamo
def cotizar_prestamo():
    tipo_prestamo = int(valoresPres.get()[0])
    nombre = entryNombre.get()
    edad = int(entryEdad.get())
    genero = 'M' if valoresGen.get() == '1' else 'F'
    condicion = 'S' if comboCondicion.get() == 'FUMADOR' else 'N'
    monto_prestamo = float(entryMontoPres.get())
    plazo_anual = int(entryPlazoAño.get())
    
    # Tasa de interés según tipo de préstamo
    if tipo_prestamo == 1:
        tasa_interes = 0.06
    elif tipo_prestamo == 2:
        tasa_interes = 0.13
    else:
        tasa_interes = 0.09

    # Calcular cuota mensual
    cuota_mensual = obtenerLM(monto_prestamo, tasa_interes, plazo_anual)
    LetraMen.set(f"{cuota_mensual:.2f}")
    
    # Calcular prima de seguro de vida
    prima_vida = obtenerPrimaVida(monto_prestamo, edad, genero, condicion)
    Poliza.set(f"{prima_vida:.2f}")

# Crear ventana principal
ventana = Tk()
ventana.title('Modulo de Prestamo')

miframe = Frame()
miframe.pack(side='top', fill='x')

miframe.config(background='steelblue4', width='600', height='40')
milabel = Label(miframe, text='MODULO DE PRÉSTAMOS', background='steelblue4', font=("Helvetica", 12, "bold")).pack()

# Labels y campos de entrada
Label(ventana, text='Tipo de Préstamo ', font=("Helvetica", 12, "bold")).place(x=40, y=70)
Label(ventana, text='Nombre Completo ', font=("Helvetica", 12, "bold")).place(x=40, y=120)
Label(ventana, text='Edad ', font=("Helvetica", 12, "bold")).place(x=450, y=120)
Label(ventana, text='Genero ', font=("Helvetica", 12, "bold")).place(x=40, y=170)
Label(ventana, text='Condición ', font=("Helvetica", 12, "bold")).place(x=450, y=170)
Label(ventana, text='Monto del Préstamo ', font=("Helvetica", 12, "bold")).place(x=40, y=220)
Label(ventana, text='Plazos (en años) ', font=("Helvetica", 12, "bold")).place(x=450, y=220)

# Botón para calcular
Button(ventana, text='Calcular Letra Mensual', command=cotizar_prestamo, bg='darkgray', font=("Helvetica", 12)).place(x=40, y=350)

# Labels para mostrar resultados
Label(ventana, text='Letra Mensual', font=("Helvetica", 12, "bold")).place(x=450, y=350)
Label(ventana, text='Póliza de Vida', font=("Helvetica", 12, "bold")).place(x=450, y=400)

# Combobox para selección del tipo de préstamo
valoresPres = StringVar()
ttk.Combobox(ventana, textvariable=valoresPres, width=27, values=('1. Hipotecario', '2. Personal', '3. Auto')).place(x=220, y=70)

# Campos de entrada
entryNombre = Entry(ventana, width=30)
entryNombre.place(x=220, y=120)

entryEdad = Entry(ventana, width=18)
entryEdad.place(x=550, y=120)

entryMontoPres = Entry(ventana, width=30)
entryMontoPres.place(x=220, y=220)

entryPlazoAño = Entry(ventana, width=10)
entryPlazoAño.place(x=600, y=220)

# Radiobutton para género
valoresGen = StringVar()
Radiobutton(ventana, text='Masculino', variable=valoresGen, value='1').place(x=220, y=170)
Radiobutton(ventana, text='Femenino', variable=valoresGen, value='2').place(x=320, y=170)

# Combobox para condición de fumador/no fumador
condicion = StringVar()
comboCondicion = ttk.Combobox(ventana, textvariable=condicion, width=15, values=('FUMADOR', 'NO FUMADOR'))
comboCondicion.place(x=550, y=170)

# Variables para mostrar resultados
LetraMen = StringVar()
Entry(ventana, textvariable=LetraMen, width=15).place(x=570, y=350)

Poliza = StringVar()
Entry(ventana, textvariable=Poliza, width=15).place(x=570, y=400)

# Configuración de la ventana
ventana.geometry('700x500')
ventana.mainloop()

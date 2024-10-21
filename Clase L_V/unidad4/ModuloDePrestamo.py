from tkinter import *
from tkinter import ttk

def obtenerLM(monto_prestamo, tasa_interes, plazo_anual):
    tasa_mensual = tasa_interes/12
    num_pagos = plazo_anual * 12
    cuota_mensual = monto_prestamo * (tasa_mensual / (1 - (1 + tasa_mensual)**(-num_pagos)))
    return cuota_mensual

def obtenerPrimaVida (monto_prestamo, edad, genero, condicion):
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

def cotizar_prestamo():
    tipo_prestamo = int(valoresPres.get()[0])
    nombre = entryNombre.get()
    edad = int(entryEdad.get())
    genero = 'M' if valoresGen.get() == '1' else 'F'
    condicion = 'S' if combo.get() == 'FUMADOR' else 'N'
    monto_prestamo = float(entryMontoPres.get())
    plazo_anual = int(entryPlazoAño.get())
    
    if tipo_prestamo == 1:
        tasa_interes = 0.06
    elif tipo_prestamo == 2:
        tasa_interes = 0.13
    else:
        tasa_interes = 0.09


    cuota_mensual = obtenerLM(monto_prestamo, tasa_interes, plazo_anual)
    LetraMen.set(f"{cuota_mensual:.2f}")
    
    # Calcular prima de seguro de vida
    prima_vida = obtenerPrimaVida(monto_prestamo, edad, genero, condicion)
    Poliza.set(f"{prima_vida:.2f}")



ventana = Tk()

ventana.title('Modulo de Prestamo')

miframe = Frame()
miframe.pack(side='top')

miframe.config(background='steelblue4', width='600', height='40')
milabel = Label(miframe, text='MODULO DE PRÉSTAMOS', background='steelblue4', font=("Helvetica", 12, "bold")).place(x=15, y=15)

lbltipo = Label(ventana, text='Tipo de Préstamo ', font=("Helvetica", 12, "bold")).place(x=40, y=70)
lblnombre = Label(ventana, text='Nombre Completo ',font=("Helvetica", 12, "bold")).place(x=40, y=120)
lbledad = Label(ventana, text='Edad ', font=("Helvetica", 12, "bold")).place(x=450, y=120)
lblgenero = Label(ventana, text='Genero ', font=("Helvetica", 12, "bold")).place(x=40, y=170)
lblcondicion = Label(ventana, text='Condición ', font=("Helvetica", 12, "bold")).place(x=450, y=170)
lblMontoPres = Label(ventana, text='Monto del Préstamo ', font=("Helvetica", 12, "bold")).place(x=40, y=220)
lblplazosaños = Label(ventana, text='Plazos (en años) ', font=("Helvetica", 12, "bold")).place(x=450, y=220)

boton = Button(ventana, text='Calcular Letra Mensual', command=cotizar_prestamo, bg='darkgray', font=("Helvetica", 12)).place(x=40, y=350)
lblletra = Label(ventana, text='Letra Mensual', font=("Helvetica", 12, "bold")).place(x=450, y=350)
lblpoliza = Label(ventana, text='Póliza de Vida', font=("Helvetica", 12, "bold")).place(x=450, y=400)


valoresPres = StringVar()
combo = ttk.Combobox(ventana, textvariable=valoresPres, width=27, values=('1. Hipotecario', '2. Personal', '3. Auto')).place(x=220, y=70)

entryNombre = Entry(ventana, width=30)
entryNombre.place(x=220, y=120)

valoresGen = StringVar()
combo1 = ttk.Radiobutton(ventana, text='Masculino', variable=valoresGen, value=1, command='selection').place(x=200, y=170)
combo2 = ttk.Radiobutton(ventana, text='Femenino', variable=valoresGen, value=2, command='selection').place(x=300, y=170)

condicion = StringVar()
combo = ttk.Combobox(ventana, textvariable=condicion, width=15, values=('FUMADOR', 'NO FUMADOR'))
combo.place(x=550, y=170)

entryEdad = Entry(ventana, width=18)
entryEdad.place(x=550, y=120)

entryMontoPres = Entry(ventana, width=30)
entryMontoPres.place(x=220, y=220)

entryPlazoAño = Entry(ventana, width=10)
entryPlazoAño.place(x=600, y=220)

LetraMen = StringVar()
entryLetraMen = Entry(ventana, textvariable=LetraMen, width=15).place(x=570, y=350)

Poliza = StringVar()
entryPoliza = Entry(ventana, textvariable=Poliza, width=15).place(x=570, y=400)


ventana.geometry('700x500') 
ventana.mainloop()
"""
Se solicita calcular el monto de impuesto sobre la renta de Personas naturales, 
para esto debe pedir el total de los ingresos del año y luego el total de los gastos del año.    
Debe aplicar la resta para identificar cual es la ganancia neta del año. 
Ganacia Neta = Ingreso del Año - Gastos del Año.....
"""

def ImpuestoSobreRenta(IngresoDA, GastosA):
    #Ganacia de año
    GanaciaN = IngresoDA - GastosA
    
    #condiciones
    if GanaciaN < 0:
        PorcImpuesto = 0
    elif GanaciaN <= 11000:
        PorcImpuesto = 0
    elif GanaciaN <= 50000:
        PorcImpuesto = 0.15
    else:
        PorcImpuesto = 0.25

    impuesto = GanaciaN * PorcImpuesto

    return impuesto

#Mensajes para ingresar datos
IngresoDA = float(input(f'Indique su Ingreso anual: '))
GastosA = float(input(f'Indique sus Gastos anual: '))  

#Calculamos el impuesto
impuesto = ImpuestoSobreRenta(IngresoDA, GastosA)

#Salida del programa
print(f'Su impuesto sobre la renta es: B./{impuesto:.2f}')
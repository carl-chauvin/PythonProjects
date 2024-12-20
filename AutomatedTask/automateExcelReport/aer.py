""" Automatizacion de Informes de Excel con Python """

# importar las librerias Pandas(Para manipular Datos) 
# y Openpyxl(Para crear graficos, tablas y realizar calculos en Excel)
import pandas as pd
import openpyxl

from openpyxl import load_workbook #para cargar la hoja de calculo
from openpyxl.styles import Font #para dar el estilo de las letras de la hoja
# Barchart para la creacion de graficos y Reference para definir rangos de celdas en una hoja de Excel que serán la base de datos del gráfico.
from openpyxl.chart import BarChart, Reference 
import string # para el tipo de datos

#Para leer el archivo Excel
excelFile = pd.read_excel("supermarket_sales.xlsx")

#las columnas que necesitamos para el informe
excelFile[["Gender", "Product Line","Total"]]

#Para crear la Tabla Dinamica, use la función .pivot_table()
reportTable = excelFile.pivot_table(
    index="Gender", #genero
    columns="Product Line", #linea de producto
    values="Total", #el total de dinero gastado por hombres y mujeres en las diferentes líneas de productos 
    aggfunc="sum" #para la sumatoria de los puntos en las columnas agrupadas
).round(0) #para retorno nulo

display(reportTable) #muestra el resultado
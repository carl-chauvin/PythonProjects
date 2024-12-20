#conectar python con una base de datos MSSQL
import pymssql #Ya descargue la libreria pymssql, ahora la importamos


#usaremos la funcion .connect() para conectar a la base de datos
conn = pymssql.connect(
    server='Carl_Chauvin\SQLEXPRESS', #host de la base de datos
    user='!cchauvin', #usuario de la base de datos para conectarse como
    password='Carl5991@', #contraseña del usuario
    database='AdventureWorks', #la base de datos con la que se inicializará la conexión.
    as_dict=True #indica si las filas se deben devolver como diccionarios en lugar de tuplas.
)

#La consulta que haremos en la base de datos de MSSQL
SQL_QUERY = '''
SELECT ST.Name AS Name, SUM(TotalDue) AS TOTAL_SALES
FROM Sales.SalesOrderHeader SOH
LEFT JOIN Sales.SalesTerritory ST
ON SOH.TerritoryID = ST.TerritoryID
WHERE SOH.TerritoryID IS NOT NULL
GROUP BY ST.Name
HAVING SUM(TotalDue) > 10000000
'''
#declare una variable cursor y use la funcion .execute para ejecutar la consulta
cursor = conn.cursor()
cursor.execute(SQL_QUERY)

#Use cursor.fetchall con un loop foreach para obtener todos los registros de la base de datos.
records = cursor.fetchall() 
for r in records:
    print(f"{r['Name']}\t{r['TOTAL_SALES']}")
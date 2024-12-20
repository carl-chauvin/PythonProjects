""" Input Datasheet into webforms autimaticaly """
#Importe las bibliotecas necesarias para la automatizacion web y manipulacion de Excel

# Modulo principal para controlar navegadores
from selenium import webdriver 

# Importa Service, que administra el controlador (chromedriver) necesario para interactuar con Chrome
from selenium.webdriver.chrome.service import Service 

# Importa ChromeDriverManager, que descarga y actualiza automáticamente el controlador para Google Chrome
from webdriver_manager.chrome import ChromeDriverManager 

# Importa "By", que proporciona métodos para localizar elementos en una página web (por ID, XPATH, CSS, etc.)
from selenium.webdriver.common.by import By 

# Importa "expected_conditions", que contiene condiciones para esperar eventos específicos (como elementos visibles)
from selenium.webdriver.support import expected_conditions as EC

# Importa WebDriverWait, que permite definir tiempos de espera explícitos para manejar elementos dinámicos
from selenium.webdriver.support.ui import WebDriverWait 

# Importa TimeoutException, que se utiliza para manejar errores de tiempo de espera cuando un elemento no está disponible
from selenium.common.exceptions import TimeoutException

from openpyxl import load_workbook #Para trabajar con archivos Excel
import time # Para introducir pausas en la ejecución

# Cargar el archivo de Excel que contiene los datos
wb = load_workbook(filename='data.xlxs') # Para cargar el archivo Excel
ExcelSheet = ['Sheet1'] # Selecciona la hoja "Sheet1" del archivo data.xlxs en Excel

#Configurando el navegador Chrome para la automatizacion
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Instala y unitiliza el navegador Chrome

# Abrir la página web de tablas y configurar el navegador
driver.get('www.webpagetable.com') # Abre la pagina con tablas interactivas
driver.maximize_window() # Maximiza la ventana del navegador
driver.implicitly_wait(10) #Espera implicitamente 10s para que los elementos de la pagina se carguen

# Inicio del bucle para iterar sobre las filas del archivo Excel
i = 2 #Para empiece a tomar los datos desde la 2nda fila(suponiendo que la 1era es el encabezado)

while i <= len(ExcelSheet[A]): # Recorre todas las filas con datos en la columna A
    FirstName = ExcelSheet["A" + str(i)].value #Nombre
    LastName = ExcelSheet["B" + str(i)].value #Apellido
    Email = ExcelSheet["C" + str(i)].value #Correo
    Age = ExcelSheet["D" + str(i)].value #Edad
    Salary = ExcelSheet["E" + str(i)].value #Salario
    Department = ExcelSheet["F" + str(i)].value #Departamento

    # Para hacer click en el botón "Add New Record" para abrir el formulario
    driver.find_element(By, ID, "addNewRecordButton").click()

    try:
        # Espera explícita para verificar que el formulario es visible
        WebDriverWait(driver, 10).until(EC.visibility_of_elements_located((By.XPATH,"/html/body/div[4]/div/div(ejemplo)")))

        # Para llenar los campos del formulario con los datos extraidos del archivo Excel
        driver.find_element(By.ID, "firstname").send_keys(FirstName)
        driver.find_element(By.ID, "lastname").send_keys(LastNameName)
        driver.find_element(By.ID, "username").send_keys(Email)
        driver.find_element(By.ID, "age").send_keys(Age)
        driver.find_element(By.ID, "salary").send_keys(Salary)
        driver.find_element(By.ID, "department").send_keys(Department)

    except TimeoutException:
        # Si el formulario no aparece, imprimira un mensaje de error
        print("The Form has not been loaded correctly, please try again.")
        pass

    time.sleep(1) # Tardara 1s para entre iteraciones
    i+=1 #Para pasar a la siguiente fila de archivo excel

# Mensaje al completar todas las iteraciones
print("The form has been filled successfully.")
time.sleep(20) #Espera 20 segundos antes de cerrar el navegador
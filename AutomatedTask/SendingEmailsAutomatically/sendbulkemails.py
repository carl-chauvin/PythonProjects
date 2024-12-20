import csv  # Importa el módulo para trabajar con archivos CSV (estructurados, similares a una tabla o Excel)
import os  # Importa el módulo para interactuar con el sistema operativo (aunque no se usa en este código)
import smtplib  # Importa el módulo para enviar correos electrónicos mediante el protocolo SMTP
import ssl  # Importa el módulo para crear un contexto SSL, que asegura la conexión en redes

# Configuración del servidor y autenticación para enviar correos
SMTP_SERVER = 'smtp.gmail.com'  # Define el servidor SMTP de Gmail para enviar correos electrónicos
EMAIL = 'drizyboyyoung@gmail.com'  # Email del remitente que usará para iniciar sesión en el servidor
PASSWORD = 'pbel ukhy gxqk xnqv'  # Contraseña de aplicación del remitente (debe ser protegida y no compartida)
PORT = 587  # Puerto que permite enviar correos electrónicos de forma segura usando TLS(Transport Layer Security)

# Crear un contexto SSL para encriptar la conexión
context = ssl.create_default_context()  # Crea un contexto de conexión segura (SSL = Secure Socket Layer) para proteger los datos

# Establece conexión con el servidor SMTP(Simple Mail Transfer Protocol) de Gmail en el puerto seguro 587
with smtplib.SMTP(SMTP_SERVER, PORT) as server:  
    server.starttls(context=context)  # Inicia la conexión TLS, encriptando los datos de inicio de sesión
    server.login(EMAIL, PASSWORD)  # Autentica al remitente con el correo y la contraseña

    # Abre el archivo 'receivers.csv' en modo lectura ('r')
    with open('receivers.csv', 'r') as file:  
        reader = csv.reader(file)  # Lee el archivo CSV utilizando el lector CSV de Python
        next(reader)  # Salta la primera fila (cabecera) para evitar interpretarla como un registro

        # Itera a través de cada fila del CSV, extrayendo los datos en las variables correspondientes
        for name, email, designation, salary in reader:
            # Define el mensaje del correo, con el destinatario y los detalles específicos de su posición y salario
            message = f'''\n
            Subject: Mi primer correo

            Felicidades {name}, 
            
            Felicidades, este correo es para informarle que fue contratado para la posición de {designation}.
            Devengando un salario de {salary}.

            Atentamente,
            ''' 
            # Envía el correo con el mensaje al email del destinatario usando la función sendmail()
            server.sendmail(EMAIL, email, message)

# Muestra un mensaje en consola al completar el envío
print('Correo Enviado!')
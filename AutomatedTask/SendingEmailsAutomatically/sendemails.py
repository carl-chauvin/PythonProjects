import os  # Importa el módulo para interactuar con el sistema operativo
import smtplib  # Importa el módulo para enviar correos electrónicos mediante el protocolo SMTP
import ssl  # Importa el módulo para crear un contexto SSL, que asegura la conexión en redes

# Configuración del servidor SMTP, email y puerto
SMTP_SERVER = 'smtp.gmail.com'  # Servidor SMTP de Gmail para enviar correos
EMAIL = 'drizyboyyoung@gmail.com'  # Dirección de correo electrónico del remitente
PASSWORD = 'pbel ukhy gxqk xnqv'  # Contraseña de aplicación para autenticar el correo del remitente
PORT = 587  # Puerto 587 para conexión segura mediante TLS
# También podría usarse el puerto 465, que es específico para conexiones SSL por defecto

# Crear un contexto SSL para asegurar la conexión
context = ssl.create_default_context()  # Contexto SSL para encriptar los datos de la conexión

# Establecer conexión con el servidor SMTP
with smtplib.SMTP(SMTP_SERVER, PORT) as server:  
    server.ehlo()  # Identifica la conexión al servidor SMTP
    server.starttls(context=context)  # Activa TLS para encriptar la conexión de datos
    server.ehlo()  # Vuelve a identificar la conexión, aunque no es obligatorio ya que starttls() la llama automáticamente

    # Inicia sesión en el servidor SMTP de Gmail con las credenciales encriptadas
    server.login(EMAIL, PASSWORD)  

    # Definir el mensaje de correo
    MESSAGE = '''\n 
        Subject: Mi primer correo

        Hola, 
        
        Me llamo Carl Chauvin y este es mi primer correo con Python.

        Atentamente,
        ''' 

    # Enviar el correo
    server.sendmail(EMAIL, 'nandy239@outlook.es', MESSAGE)  # Usa sendmail() para enviar el mensaje al destinatario

    # Mensaje de confirmación en consola
    print('Correo enviado correctamente!')  # Informa al usuario que el correo fue enviado

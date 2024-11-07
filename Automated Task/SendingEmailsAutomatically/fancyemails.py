import os  # Importa el módulo para interactuar con el sistema operativo
import smtplib  # Importa el módulo para enviar correos electrónicos mediante el protocolo SMTP
import ssl  # Importa el módulo para crear un contexto SSL, que asegura la conexión en redes

# Módulos para construir el correo con archivos adjuntos
from email import encoders  # Para codificar archivos adjuntos en base64
from email.mime.base import MIMEBase  # Base del correo para construir el mensaje con adjuntos
from email.mime.multipart import MIMEMultipart  # Permite crear correos con múltiples partes (texto, adjuntos)
from email.mime.text import MIMEText  # Permite agregar texto en el cuerpo del correo

# Configuración del servidor SMTP, email y puerto
SMTP_SERVER = 'smtp.gmail.com'  # Define el servidor SMTP de Gmail
EMAIL = 'drizyboyyoung@gmail.com'  # Email del remitente para iniciar sesión en el servidor
PASSWORD = 'pbel ukhy gxqk xnqv'  # Contraseña de aplicación del remitente (debe protegerse y no compartirse)
PORT = 587  # Puerto seguro para enviar correos con TLS

# Contenido del correo
subject = 'Mi segundo mensaje'  # Asunto del correo
body = 'Espero que puedan ver el documento adjunto en el correo'  # Texto del cuerpo del mensaje
receiver_email = 'chauvin239@gmail.com'  # Dirección de correo del destinatario

# Crear el mensaje de correo con múltiples partes
mensaje = MIMEMultipart()  # Instancia que permite agregar varias partes al correo
mensaje['From'] = EMAIL  # Añade el remitente al correo
mensaje['To'] = receiver_email  # Añade el destinatario al correo
mensaje['Subject'] = subject  # Añade el asunto del correo

mensaje.attach(MIMEText(body, 'plain'))  # Adjunta el cuerpo de texto simple al mensaje

# Adjuntar el archivo
filename = 'imagen.jpg'  # Nombre del archivo a adjuntar

# Abrir y leer el archivo en modo binario
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')  # Define el tipo de contenido como archivo binario
    part.set_payload(attachment.read())  # Lee el archivo y lo adjunta como carga útil

# Codifica el archivo adjunto en base64 para enviarlo por correo
encoders.encode_base64(part)  # Convierte el archivo a base64 para asegurar la compatibilidad

# Añade los encabezados de archivo adjunto
part.add_header(
    'Content-Disposition',  # Encabezado que define la disposición del contenido adjunto
    f'attachment; filename={filename}',  # Adjunta el archivo con el nombre especificado
)

# Adjunta el archivo codificado al mensaje
mensaje.attach(part)  # Agrega el archivo adjunto al mensaje de correo
text = mensaje.as_string()  # Convierte el mensaje completo a una cadena de texto

# Crear el contexto SSL para asegurar la conexión
context = ssl.create_default_context()  # Crea un contexto SSL para proteger la conexión

# Conectar y enviar el correo
with smtplib.SMTP(SMTP_SERVER, PORT) as server:  # Conecta al servidor SMTP de Gmail
    server.starttls(context=context)  # Inicia una conexión TLS encriptada
    server.login(EMAIL, PASSWORD)  # Inicia sesión con las credenciales del remitente
    server.sendmail(EMAIL, receiver_email, text)  # Envía el correo con el mensaje y adjunto

# Confirmación en consola
print('Correo Enviado!')

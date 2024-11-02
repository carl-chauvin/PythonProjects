import os #sirve para interactuar con el sistema operativo
import smtplib #modulo usado para el envio de los correos
import ssl #metodo para encriptar las credenciales

SMTP_SERVER = 'smtp.gmail.com'
EMAIL = 'drizyboyyoung@gmail.com' #os.environ.get('EMAIL') #variable que almacena el correo
PASSWORD = 'pbel ukhy gxqk xnqv'#os.environ.get('PASSWORD') #variable que almacena la contraseña
PORT = 587 #este puerto sirve para enviar correos electronicos de forma segura con TLS
#465 #se usa este puerto(465) por defecto para encriptar la comunicación

context = ssl.create_default_context()

with smtplib.SMTP(SMTP_SERVER, PORT) as server:
    server.ehlo() #indetificarme en el servidor
    server.starttls(context=context) #proteje y sostiene la conexión
    server.ehlo() #indetificarme de nuevo en el servidor // pero no es obligatorio ya que la funcion ".starttls()" la llama automaticamente
    server.login(EMAIL,PASSWORD) #sirve para asegurar la conexión al servidor Gmail SMTP usando la direccion del servidor y el puerto SSL para asegurar que los credenciales esten encriptados
    #la variable mensaje contiene el texto del correo.
    MESSAGE = '''\n 
        Subject: Mi primer correo

        Hola, 
        
        Me llamo Carl Chauvin y este es mi primer correo con python.

        Atentamente,
        ''' 
    server.sendmail(EMAIL,'nandy239@outlook.es', MESSAGE) #usamos la funccion sendmail() para enviar los correos.
    print('Correo enviado correctamente!') #sirve para confirmar el envio del correo
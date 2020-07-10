import os 
from twilio.rest import Client

#
# ES NECESARIO REGISTRO EN WEB DE TWILIO
#
account_sid = '-------------------------------' # SE OBTIENE AL REGISTAR EN TWILIO
auth_token = '--------------------------------' # SE OBTIENE AL REGISTAR EN TWILIO
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886', # NUMERO QUE ENVÍA EL MENSAJE
                              body='*ALERTA*',  # MENSAJE
                              media_url='https://i.ibb.co/tCKvds8/logo-shielder-colors.png',  # IMAGEN OPCIONAL                           
                              to='whatsapp:+ AQUÍ NUMERO REGISTRADO' # NUMERO DE DESTINATARIO
                          ) 
                        
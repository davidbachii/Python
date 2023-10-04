# -*- coding: utf-8 -*-
from socket import *

#El servidor del correo al que nos vamos a conectar
serverName = '127.0.0.1' 	# Introducir la direccion del servidor que proporcione el profesor.
serverPort = 8888			# Introducir el puerto del servidor que proporcione el profesor.

#Mensaje que vamos a enviar, Los mensajes de correo deben terminar con una linea que solo contenga el caracter '.'
msg = 'Hola mundo'	#Variable que alamacena el mensaje que se desea enviar
endLine = "\r\n.\r\n"				#No Tocar, es la indicación de final de mensaje

#Datos de envio básicos
Mail_Scr = "MAIL FROM:puestoLE12P09@ar1.es\r\n" 		#MODIFICAR la X por el numero de puesto
Mail_Dst = "RCPT TO:ar1@gpar1.es\r\n"			#NO MODIFICAR

#Lista que contiene la secuencia ordenada de comando a enviar
secuencia_de_comandos = ['HELO LE12P09\r\n', Mail_Scr, Mail_Dst, 'DATA\r\n', msg, 'QUIT\r\n'];
#Lista que contiene la secuencia ordenada de codigos a recibir
codigo_a_recibir = ['250','250','250','354','254','221'];

#Mensaje de error
Error = 'No se ha recibido el código de respuesta esperado';	#NO MODIFICAR

#Creamos el socket y nos conectamos al servidor
clientSocket = socket (AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

recv1 = clientSocket.recv(1024)
#220 NOMBRE_SERVIDOR Python SMTP proxy version 0.2
print (recv1.decode())

for i in range(0, len(secuencia_de_comandos)):
	
	#enviamos el comando deseado
	clientSocket.send(secuencia_de_comandos[i].encode());
	print(secuencia_de_comandos[i])
	#En el caso de que el comando enviado lo requiera
	if (i == 4):
		#Debemos enviar la indicacion de final de mensaje
		clientSocket.send(endLine.encode())
		
	#esperamos respuesta
	recv1 = clientSocket.recv(1024)
	#sacamos por pantalla el mensaje recibido
	print (recv1.decode())
	#analizamos los 3 primeros caracteres del mensaje con lo recibido
	if recv1[:3].decode() != codigo_a_recibir[i]:
		#en caso de no ser lo esperado paramos
		print (Error)
		exit
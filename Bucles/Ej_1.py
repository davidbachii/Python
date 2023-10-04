#Comprobar si una direccion de correo electronico es verdadera o no
seguir = True
email = False
while seguir:
    direccion = input("Introduzca una direccion de correo :")
    for i in direccion: #Va a recorrer la palabra caracter por caracter
        if i == '@':
         email = True
    if email == True:
     print("Email itroducido correctamente")
     seguir = False
    else:
        print("Email mal introducido")
        seguir = True

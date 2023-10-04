'''
Pedir un caracter y determinar si ese caracter introducido es igual a una vocal
'''

caracter = input("Introduzca un caracter: ").lower() #Pide al usuario un caracter y lo transforma a una minuscula asi en este caso
#me leeria tanto las mayusculas como las minusculas


if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
    print("El caracter introducido es una vocal")
else:
    print("El caracter introducido no es una vocal")
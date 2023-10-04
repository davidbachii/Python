n1 = float(input("Introduzca el primer numero de la operacion: "))
n2 = float(input("Introduzca el segundo numero de la operacion: "))

operacion = input("Escriba la operacion que desea realizar: ").upper() #Transforma el caracter a mayuscula
'''
S,s --> suma
R,r -->resta
P,p,M,m -->multiplicacion
'''

if operacion == 'S':
    suma = n1 + n2
    print(f"La suma es {suma}")
elif operacion == 'R':
    resta = n1 - n2
    print(f"La resta es {resta}")
elif operacion == 'P' or 'M':
    mult = n1 * n2
    print(f"La multiplicacion es {mult}")
else:
    print("El caracter introducido no es correcto")

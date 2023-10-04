'''
Programa que pida tres numeros y determine cual es el mayor
'''

n1 = int(input("Introduzca el numero 1:"))
n2 = int(input("Introduzca el numero 2:"))
n3 = int(input("Introduzca el numero 3:"))


if n1>n2>n3:
    print(f" {n1} es el numero mayor")
elif n2>n1>n3:
    print(f" {n2} es el numero mayor")
else:
    print(f" {n3} es el numero mayor")
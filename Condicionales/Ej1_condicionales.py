'''
Pedir dos numeros y saber cual de ellos es par o si ambos son o no son pares
'''

n1 = int(input("Introduzca el primer numero: "))
n2 = int(input("Introduzca el segundo numero: "))


if n1%2 == 0 and n2%2 == 0:
    print("Ambos numeros son pares")
elif n1%2 == 0 and n2%2!=0:
    print(f"El {n1} es par")
elif n1 % 2 != 0 and n2 % 2 == 0:
    print(f"El {n2} es par")
else:
    print("ningun numero es par")

'''
Escribe un programa que lea una serie de números enteros hasta que se
introduzca el número -9999, y cuente el total de números introducidos, el total de
valores positivos y el total de valores negativos (no consideres el cero ni positivo ni
negativo). Reutiliza la función que hayas diseñado en el Ejercicio 1 para validar tus
entradas.
'''

contador = 0
numero = 0
positivos = 0
negativos = 0
nulos = 0

while numero != -9999:
    numero = int(input("Introduzca un numero: "))
    contador+=1
    if numero > 0:
        positivos+= 1
    elif numero < 0:
        negativos += 1
    else:
        nulos += 1

print(f"Total de numeros introducidos: {contador}"
      f"\n Total de numeros positivos: {positivos}"
      f"\n Total de numeros negativos: {negativos}")

'''
Escribe un programa que, después de preguntar ¿Cuántos números se van a
introducir?, pida esos números (enteros o reales) y devuelva su media aritmética,
el mayor y el menor. El programa debe controlar que la cantidad de números es
mayor de 2 y en caso contrario ha de mostrar un mensaje de error. Como siempre,
valida las entradas.
'''
contador = 1
numeros = 0

seguir = True
while seguir:
    n = int(input("¿Cuantos numeros va a introducir? :"))
    if n > 2:
        numero = int(input("Introduce un numero:"))
        mayor = numero
        menor = numero
        for i in range (n-1):
            n_1=int(input("Introduzca un numero entero o real: "))
            numeros += n_1 + numero
            contador += 1
        if n_1  > numero:
            mayor = n_1
        elif n_1 < numero:
            menor = n_1
        media = (numeros/contador)
        print(f"La media artimetica es: {media}")
        print(f"El mayor es: {mayor}")
        print(f"El menor es : {menor}")
        seguir = False
    else:
        print("El numero es menor de dos no es valido")
        seguir = True

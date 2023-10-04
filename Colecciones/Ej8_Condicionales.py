'''
Realizar un programa que lea palabras hasta que se introduzca “fin”,
mostrando un recuento de las longitudes de las palabras, es decir, el
número total de palabras de longitud 1 que se hayan introducido, el total de
longitud 2, etc. La máxima longitud de las palabras deberá ser de 15
caracteres. Una posible salida de este programa sería:
'''
seguir = True
while seguir:
    n = input("Introduce una palabra: ")
    if n == 'fin':
        seguir = False
    else:
        for i in range(15):
                if len(n) == i:
                 print(f"Palbras de longitud {i}")



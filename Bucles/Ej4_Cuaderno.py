'''
Escribe un programa que lea un entero positivo n y genere una tabla con las n
primeras potencias de 2, 3 y 5. Así:
1 2 4 8 16 32 64 ...
1 3 9 27 81 243 729 ...
1 5 25 125 625 3125 15625 ...
'''

n = int(input("Introduce un entero positivo: "))
if n > 0:
    for i in[2,3,5]:
        for j in range(n):
            print(f"{i**j}",end=" ")
        print()
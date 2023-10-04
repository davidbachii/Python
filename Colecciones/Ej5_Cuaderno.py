'''
Una lista de enteros original debe utilizarse para generar dos listas, una con
los números pares de la original ordenados ascendentemente y otra con los
impares ordenados descendentemente. La generación de las 2 listas debe
hacerse a medida que se recorre la original, es decir, se toma un número de
la original, se decide a qué lista (pares o impares) debe ir, y se inserta
ordenado en la misma de acuerdo con el criterio de la lista (ascendente o
descendente).
'''
import random
lista_original = []
listas_pares = []
lista_impares = []


for i in range(8):
    lista_original += [random.randint(1,12)]
for i in lista_original:
    if i % 2 == 0:
        listas_pares += [i]
    elif i % 2 != 0:
        lista_impares += [i]

listas_pares.sort() #Ordena la lista de menor a mayor
lista_impares.sort(reverse=True) #Ordena la lista de mayor a menor

print(lista_original)
print(f"Lista de pares: {listas_pares}"
      f"\n Lista de impares: {lista_impares}")
'''
Crear una lista de enteros, inicializarlos según valores aleatorios en el rango
1..20 y computar la media de los valores, el valor más alto y el más bajo (todo
ello utilizando listas).

'''

import random
#Para generar listas con valores aleatorios
lista_enteros = []
for i in range(10):
    lista_enteros += [random.randint(1, 20)]
maximo = lista_enteros[0]
minimo = lista_enteros[0]
suma = 0

for i in lista_enteros:
    suma += i
    if i < minimo:
        minimo = i
    elif i > maximo:
        maximo = i
media = (suma/len(lista_enteros))

print(lista_enteros)
print(media)
print(f"El maximo es {maximo}, el minimo es {minimo}")



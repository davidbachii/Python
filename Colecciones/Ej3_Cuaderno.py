'''
Modificar una lista de números reales que representan las calificaciones de los
alumnos de una clase, para sustituir los valores numéricos por sus
calificaciones alfanuméricas (Suspenso, Aprobado, etc.)

'''
import random

lista = []
lista_alfanumerica = []

for i in range(7):
    lista += [random.randint(0,10)]

for i in lista:
    if i >= 9:
        lista_alfanumerica += ['sobresaliente']
    elif 7 <= i < 9:
        lista_alfanumerica += ['notable']
    elif 6<= i <7:
        lista_alfanumerica += ['bien']
    elif 5 <= i < 6:
        lista_alfanumerica += ['suficiente']
    else:
        lista_alfanumerica += ['suspenso']

print(lista)
print(lista_alfanumerica)


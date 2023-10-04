'''
Escriba un programa modularizado en Python que genere 5 frases a partir de
palabras en la siguiente lista:
['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']
Las frases, que deben tener entre 3 y 10 palabras, deben generarse eligiendo un
número aleatorio de palabras cada vez, de modo que la primera frase puede tener
3 palabras, mientras que la segunda podría tener 6 palabras. Una vez generada
una frase, el programa la mostrará por pantalla. Y así hasta 5 frases en total.

'''
import random
lista = ['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']

for i in range(5):
    frase = ''
    n = random.randint(3,10)
    for j in range(n):
        palabras = random.choice(lista) # Asi obtengo palbaras random de una lista
        frase += palabras + ' ' #Como va a generar entre 3 y 10 palabras las vamos almacenando en la frase vacia
    print(frase)

import random
lista = ['patata','queso','ella','yo','su mirada','rubia','morena']

for i in range(5):
    frase = ''
    n = random.randint(3,6)
    for i in range(n):
        palabra = random.choice(lista)
        frase += palabra + ' '
    print(frase)




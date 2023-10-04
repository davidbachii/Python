import random
def personaje(nombre,vida,arma,daño):
    '''
        int,int,str,int-->dict
        OBJ:Almacenar los datos del personaje en un diccionario
    '''
    return {'nombre': nombre,'vida': vida,'arma': arma,'daño': daño}
def leer_personajes():
    '''
        none-->dict
        OBJ: Leer los datos del diccionario
    '''
    nombre = input('Introduzca un nombre del personaje:')
    vida = int(input('Introduzca la vida del personaje:'))
    arma = input("Introduzca el tipo de arma del personaje:")
    daño = int(input("Introduzca el daño del personaje:"))
    return personaje(nombre,vida,arma,daño)

def ataque(personaje1,personaje2):
    '''
        OBJ:Simular el combate entre dos personajes
    '''

    combate = personaje2["vida"] - personaje1["daño"]
    if combate > 0:
        print(f'{personaje1["nombre"]} ataca a {personaje2["nombre"]} con {personaje1["arma"]}'
              f'\n le hace {personaje1["daño"]} daño y le deja a {combate} de vida')
    elif combate < 0:
        print(f'{personaje1["nombre"]} ha matado a {personaje2["nombre"]}')

def seleccionar_personajes(lista_personajes):
    '''
        list -> Personaje, Personaje
        OBJ: Selecciona aleatoriamente dos personajes distintos de entre los
        vivos. Estos personajes lucharán en esta ronda del juego.
    '''

    atacante = random.choice(lista_personajes)
    atacado = random.choice(lista_personajes)
    if atacante == atacado:
        atacante = random.choice(lista_personajes)
    return atacante,atacado



def batalla_final(lista_personajes):

    while len(lista_personajes) >= 2:

        atacante = seleccionar_personajes(lista_personajes)
        defensor = seleccionar_personajes(lista_personajes)
        print(ataque(atacante,defensor))
        if defensor['vida'] > atacante['daño']:
            print(ataque(defensor,atacante))

def menor(arma1,arma2):
    '''
        str,str-->bool
        OBJ:Ordenar a los personajes por el que tenga el arma mas tocha
    '''
    orden = ('aka-64', 'sniper', 'tactica', 'spash')
    return orden.index(arma1) <= orden.index(arma2)

def ordenar_burbuja(lista):
    '''
        list-->none
        OBJ:Ordenar la lista de personajes segun el nivel de sus armas
    '''
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if menor(lista[i]['arma'],lista[j]['arma']):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
#Probadores
lista_personajes = []



atacante = personaje('David',100,'aka-64',34)
atacado = personaje('Juan',100,'spash',90)
defensor = personaje('Raul',100,'tactica',67)
lider = personaje('Dani',100,'sniper',115)
lista_personajes.append(atacante)
lista_personajes.append(atacado)
lista_personajes.append(defensor)
lista_personajes.append(lider)


#print(lista_personajes)
print(ataque(atacante,defensor))
print('Orden inicial')
for i in lista_personajes:
    print(i)
ordenar_burbuja(lista_personajes)
print('Orden por calidad de armas')
for i in lista_personajes:
    print(i)














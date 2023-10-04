#Ejercicio 1 examen 2020
import random
def personaje(nombre,vida,nombre_arma,daño):
    '''
        str,int,str,int-->dict
        OBJ:Guardar los datos de un personaje en un diccionario
    '''
    return {'nombre':nombre, 'vida': vida, 'arma': nombre_arma, 'daño': daño}
def introducir_datos():
    '''
        dict-->none
    '''

    nombre = input('Introduce un el nombre del personaje: ')
    seguir = True
    while seguir:
            vida = int(input('Introduzca la vida del personaje: '))
            seguir = False
            if vida > 100:
                print('El valor introducido no es correcto')
                seguir = True



    nombre_arma = input('Introduzca el nombre del arma: ')
    seguir1 = True
    while seguir1:
        daño = int(input('Introduzca el daño que produce el arma en un rango de 0-125:'))
        seguir1 = False
        if daño > 125:
            print('Daño no valido ')
            seguir1 = True
    return personaje(nombre,vida,nombre_arma,daño)

def ataque(atacante,defensor):
    '''

    '''
    lista_vivos = []
    vida_final = defensor['vida'] - atacante['daño']
    print(f'{atacante["nombre"]} ataca a {defensor["nombre"]} con {atacante["arma"]}, le hace {atacante["daño"]} y le deja con '
        f'{vida_final} puntos de vida')
    lista_vivos += [atacante,defensor]
    if vida_final < 0:
        print(f'{atacante["nombre"]} ha matado a {defensor["nombre"]}')
        lista_vivos += [atacante]
    print(lista_vivos)

def seleccion_personajes(lista_personajes):
    '''
        list-->atcante,defensor
    '''

    atacante = random.choice(lista_personajes)
    defensor = random.choice(lista_personajes)
    if atacante == defensor:
        atacante = random.choice(lista_personajes)
    return atacante,defensor

def batalla(lista_personajes):
    '''
    list-->None
    OBJ:Mientras queden 2 o más personajes en la lista se repetirán los siguientes pasos: se seleccionará al atacante
        y al defensor, se simulará el ataque del atacante al defensor y, si el defensor
        sobrevive, se simulará el ataque del defensor al atacante
    '''
    while len(lista_personajes) > 2:
        atacante = seleccion_personajes(lista_personajes)
        defensor = seleccion_personajes(lista_personajes)
        if defensor['vida'] > atacante['daño']:
            print(ataque(atacante,defensor))
        elif defensor['vida'] < atacante['daño']:
            print(ataque(defensor,atacante))


#Probador
lista_personajes = []
#for i in range(2):
    #lista_personajes.append(introducir_datos())
atacante = personaje('Alfredo',100,'scar',99)
defensor = personaje('David',100,'Snipper',120)
atacante1 = personaje('Pedro',100,'spash',110)
defensor1 = personaje('Lucia',100,'tactica',80)
lista_personajes.append(atacante)
lista_personajes.append(defensor)
lista_personajes.append(atacante1)
lista_personajes.append(defensor1)
print(lista_personajes)
print(ataque(atacante, defensor))
print(seleccion_personajes(lista_personajes))
#print(batalla(lista_personajes))


#Ejercicio2
def armas(nombre,categoria,rareza):
    '''
        str,str,str-->dict
    '''
    return {'nombre': nombre, 'categoria':categoria, 'rareza':rareza}
lista_armas = []
lista_armas.append(armas('Scar','Ametralladora','Epica'))
lista_armas.append(armas('Spash','Escopeta','Legendaria'))
lista_armas.append(armas('Tactica','Escopeta','Rara'))
lista_armas.append(armas('Diggle','Rifle','Poco comun'))
lista_armas.append(armas('ray-gun','Arma de rayos','Comun'))
print(lista_armas)
def menor(rareza1,rareza2):
    '''
        str,str-->bool
    '''
    orden = ('Comun','Poco comun','Rara', 'Epica', 'Legendaria')
    return orden.index(rareza1) <= orden.index(rareza2)
def ordenar_por_rareza(lista_armas):
    '''
        list-->list
    '''
    for i in range(len(lista_armas)):
        for j in range(i+1,len(lista_armas)):
            if menor(lista_armas[i]['rareza'],lista_armas[j]['rareza']):
                aux = lista_armas[i]
                lista_armas[i] = lista_armas[j]
                lista_armas[j] = aux



ordenar_por_rareza(lista_armas)
for i in lista_armas:
    print(i)

#Ejercicio 3
def bus1_binaria_recursiva(lista,elem):
    if len(lista_armas) == 0:
        esta = False
    else:
        pto_medio = len(lista) // 2
        if lista[pto_medio] == elem:
            esta = True
        else:
            if elem < lista[pto_medio]:
                esta = bus1_binaria_recursiva(lista[:pto_medio],elem)
            else:
                esta = bus1_binaria_recursiva(lista[pto_medio +1:],elem)
    return esta
print(bus1_binaria_recursiva(['en un lugar','Juan'],'Juan'))

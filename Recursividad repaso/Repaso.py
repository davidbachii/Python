import random
def suma_listas(lista1,lista2):
    '''
        list,list-->list
        OBJ:Sumae dos listas da igual cual sea e tamaño
    '''
    if len(lista1) <= len(lista2):
        mayor = lista2
        menor = lista1
    else:
        mayor = lista1
        menor = lista1
    lista = []
    for i in range(len(menor)):
        lista += [menor[i] + mayor[i]]
    for i in range(len(menor),len(mayor)):
        lista += [mayor[i]]
    return lista

print(suma_listas([1,2,3],[1,2,3,4,6]))


def lista_pares_impares(lista):
    '''
        list-->list,list
        OBJ:Recive una lista y devuelve dos con los numeros pares e impares
    '''
    lista_pares = []
    lista_impares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares += [i]
        elif i % 2 != 0:
            lista_impares += [i]

    lista_pares.sort() #Ordenados de menor a mayor, lo mas clasico
    lista_impares.sort(reverse=True) #Ordenados de mayor a menor
    return lista_pares,lista_impares
print(lista_pares_impares([1,2,3,4,5,6,7,8,9]))

#Genero una lista y saco su maximo , su minimo y su media
lista_enteros = []
for i in range(10):
    lista_enteros += [random.randint(1,20)]
maximo = lista_enteros[0]
minimo = lista_enteros[0]
suma = 0
lista_enteros.sort()
print(lista_enteros)
for i in lista_enteros:
    suma += i
    if i < minimo:
        minimo = i
    elif i > maximo:
        maximo = i
media = suma/len(lista_enteros)

print(f'El maximo es {maximo}, el minimo es {minimo}')
print(f'La media es {media} ')

def transformar_frase(cadena):
    '''
        str-->str
        OBJ:Transformar la cadena segun los parametos indicados
    '''
    lista1 = ('a','e','i','o','u')
    lista2 = ('4','3','1','0','#') #Ojo aun que sea un numero entero para trasnformarlo solo lee strings
    cadena2 = ''
    for i in cadena:
        if i in lista1:
            cadena2 += lista2[lista1.index(i)]
        else:
            cadena2 += i
    return cadena2
print(transformar_frase('un perro del hortelano'))


for i in range(5):
    datos = ['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']
    cadena = ''
    n = random.randint(3,8)
    for i in range(n):
        cadena += random.choice(datos) + ' '
    print(cadena)




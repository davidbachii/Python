def esta_en_lista(lista,elem):
    '''
        list,int-->bool
        OBJ: Saber si un numero entero se encuentra en una lista
    '''
    if len(lista) == 0:
        esta = False

    elif lista[0] == elem:
        esta = True
    else:
        esta = esta_en_lista(lista[1:],elem)
    return esta

print(esta_en_lista([1,2,3,4,5],5))

def invertir_palbra(palabra):
    '''
        str-->str
        OBJ:Devolver el inverso de una palabra
    '''
    if palabra == '':
        resultado = ''
    else:
        resultado = invertir_palbra(palabra[1:])+palabra[0]
    return resultado
print(invertir_palbra('David'))

def contador_digitos(num):
    '''
        int-->int
        OBJ:Devolver los digitos del numero introducido
    '''
    if num < 10:
        contador = 1
    else:
        contador = contador_digitos(num//10)+1
    return contador

print(contador_digitos(23455))

def binario_recursivo(num):
    '''
        int-->str
        OBJ: Convierte un numero a binario
    '''
    if num == 0:
        resultado = ''
    else:
        resultado = binario_recursivo(num//2)+str(num%2)
    return resultado

print(binario_recursivo(234))

def busqueda_binaria_recursiva(lista,elem):
    '''
        list,str-->boll
        OBJ:Buscar una cadena dentro de una lista
    '''
    if len(lista) == 0:
        esta = False
    else:
        punto_medio = len(lista)//2
        if lista[punto_medio] == elem:
            esta = True
        else:
            if elem < lista[punto_medio]:
                esta = binario_recursivo(lista[:punto_medio],elem)
            else:
                esta = binario_recursivo(lista[punto_medio + 1:], elem)
    return esta
lista_frases = ['de cuyo nombre no quiero acordarme','en un lugar de la mancha','no ha tanto tiempo de vivia',
                'un hidalgo de los de lanza en astillero']



def sumas(lista):
    '''
        list-->none
        OBJ:Muestra pares de valores a sumar desde los extremos de una lista hacia el centro
    '''
    if len(lista) == 0:
        print(lista[0])
    else:
        print(lista[0]+ lista[len(lista) -1])
        sumas(lista[1:-1])

print(sumas([1,2,3,4]))

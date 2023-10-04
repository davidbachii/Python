'''
Escribir una función que sume dos listas de enteros de igual longitud y retorne
otra lista que contenga la suma de las originales elemento a elemento.
'''
'''
Modifica la función anterior permitiendo que las listas sean desiguales. Los
elementos sobrantes de la lista más larga se añadirán al final de la lista
resultante.
'''
#El objetivo de este ejercicio:
#En primer lugar es poder sumar listas dando igual el tamaño de ellas, solo importando el rango de la menor para su ejecucuion
#En segundo lugar es que se añada al final de la lista los elementos restantes que no estan dentro del rango de la menor
def operacion_lsitas(lista1,lista2):
    '''
        list,list-->list
        OBJ:Retornar una lista que contenga la suma de las originales
    '''
    if len(lista1) <= len(lista2):
        mayor = lista2
        menor = lista1
    else:
        mayor = lista1
        menor = lista2
    lista = []
    for i in range(len(menor)): #Le da igual que las matrices sean desiguales solo lee hasta lo que pone en el rango
        lista += [menor[i] + mayor[i]]
    for i in range(len(menor),len(mayor)):
        lista += [mayor[i]] #Añado a mi lista los elementos de la mayor
    return lista

#Probador
Lista= [2,3,4,5,8,9,7]
Lista1 = [3,4,5,6,8]
print(operacion_lsitas(Lista,Lista1))
print(operacion_lsitas([1,3,4,5,6,6],[1,2,3,4]))




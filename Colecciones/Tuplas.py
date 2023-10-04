#Tuplas

tupla = (4,"Hola",True,5.67,4) #La principal diferencia respecto a las litas es que las tuplas no se pueden modificar
#Es decir no se puede añadir elementos , ni quitar una vez creada no se podra hacer nada mas

#Lo que se puede hacer es elementos de busqueda
print(tupla.index("Hola"))
print(len(tupla))
print(tupla.count(4))

#Pasar de una lista a una tupla y de una tupla a una lista
tupla = (2,3,4,5,6)
lista = list(tupla)
print(lista)
lista = [1,2,3,4,5,6]
tupla = tuple(lista)
print(tupla)
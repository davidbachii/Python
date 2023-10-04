#Diccionarios

diccionarios = {"Rojo":"red","Azul":"blue","Verde":"green"}
print(diccionarios["Rojo"]) #Imprime red
diccionarios["Amarillo"] = "yelllow" #Lo añade a mi diccionario
print(diccionarios)
del(diccionarios["Azul"]) #Elimina todo lo correspondiente con la clave Azul de mi diccionario
print(diccionarios)

diccionarios1 = {"David":{"edad":22,"estatura":1.84},"Jose":[22,1.78]}
print(diccionarios1) #Dentro de mi diccionario puedo añadir tuplas, listas o incluso nuevos diccionarios como en el caso de david

equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo",17:"Mario Mandzukich"}
print(equipo.keys()) #Me muestra dentro de una lista las claves que hay dentro de un diccionario
print(equipo.values()) #Me muestra los valores de esas claves
print(equipo.items())#Me pone la clave y el valor de todos los elementos de mi diccionario
print(len(equipo)) #Muestra el numero de jugadores
equipo.clear()
print(equipo) #Deja vacion el diccionario


#Ejercicio1 , eliminar los elemntos repetidos de una lista

listaa = [1,2,3,"Alejandro",2,2,1,"Alejandro",3]
#Para eliminar los elementos repetidos creo un conjunto que no permite tener elementos repetidos
conjunto = set(listaa)
print(conjunto) #Ahora transformo esto de nuevo en una lista
listaa = list(conjunto)
print(listaa)

#Ejercicio 2
'''
-Crea dos listas, luego genera una lista que con los elementos que aparezcan en las dos listas
-Lista de elementos que aparecen en la primera lista, pero no en la segunda
-Lista de elementos que aparecen en la segunda lista, pero no en la primera
-Lista de elemntos que aparecen en las dos listas
'''
lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#Lo primero es hacer que las listas no tengan elementos repetidos para que no molesten
a = set(lista1)
b = set(lista2)

union = list(a | b) #Los elementos de las dos listas
elementosA = list(a - b) #Los elemntos que aparecen en la primera lista pero no en la segunda
elementosB = list(b - a) #Los elemntos que aparecen en la segunda lista pero no en la primera
interseccion = list(a & b) #Los elemntos que coinciden en las dos listas
print(f"lista que con los elementos que aparezcan en las dos listas: {union}")
print(f"Lista de elementos que aparecen en la primera lista, pero no en la segunda:{elementosA}")
print(f"Lista de elementos que aparecen en la segunda lista, pero no en la primera: {elementosB}")
print(f"Lista de elemntos que aparecen en las dos listas: {interseccion}")

#Ejercicio3 , crea tres personajes del señor de los anillos y añadelos a una lista

lista = []
personaje_1 = {"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}
personaje_2 = {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}
personaje_3 = {"Nombre":"Aragon","Clase":"Guerrero","Raza":"Dunadan del norte"}

lista.append(personaje_1)
lista.append(personaje_2)
lista.append(personaje_3)
print(lista)
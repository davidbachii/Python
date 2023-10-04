# Listas
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",True,9,[1,2,3]] #El primer dato en este caso lunes se considera que esta en la posicion 0

print(lista[0]) #Lunes
print(lista[-1]) #Seria el ultimo elemento de la lista eneste caso Viernes pero apenas se usa
print(lista[0:3]) #Me imprime los elementos de la posicion 0,1,2
print(lista[:4]) #Desde el principio hasta jueves
print(len(lista)) #Cantidad de elementos de la lista , la sublista aun que posea tres valores cuenta como un solo elemento

lista2 = [1,2,3,4,5]
lista2.append(6) #Añade el seis al final de la lista
lista2.insert(2,8) #Voy a insertar en la posicion 2, donde esta el 3 el valor 8

lista3 = [1,2,3,4,5,"David",1,2,1]
print(lista3.extend([6,7,8])) #Añade al final de la lista varios elementos
print("David" in lista3)#Me retorna un valor booleano para saber si ese elemento esa en mi lista o no
print(lista3.index(4)) #Te retorna la posicion delvaloe introducido en la lista
print(lista3.count(1)) #Cuenta cuantos unos hay en la lista
print(lista3.remove(1)) #Elimina el valor uno de mi lista
print(lista3.clear()) #Elimina los elementos de la lista y genera una lista vacia
print(lista3.reverse()) #Le da la vuelta a la lista
lista4 = [3,1,6,-3] #Lista desordemada
lista4.sort()
print(lista4)
lista4.sort(reverse=True) #Ordenaria los elementos demayor a menor
print(lista4)
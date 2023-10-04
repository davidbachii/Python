#Bucle for
#Es un bucle que recorre posicion por posicion una serie de colecciones , ya sean listas,cadenas,tuplas,diccionarios

for i in [1,2,3,4,"David"]:
    print("Hola mundo") #Esto va a imprimir hola mundo 5 veces ya que recorre la lista elemento por elemento
    print(i) #Va a imprimir uno por uno los elementos de la lista


colecciones = {"Alejandro":22,"David":18,"Miguel":25}

for i in colecciones: #Va a recorrer el diccionario
    print(f"Elementos: {i}") #Imprime las keys(Alejandro,David,Miguel)
    print(f"{colecciones[i]}") #Imprime los values(22,18,25)


#Como hacer para leer el diccionario entero
for keys,values in colecciones.items():
    print(f"{keys}-->{values}")

#El bucle for tambien puede recorrer cadenas palabra por palabra

nombre = "David"

for i in nombre: #Recorre la palabra david
    print(i,end="-") #Me va a imprimer cada letra por separado, con el end lo imprime todo en la misma linea y lo que hay
    #entre las comillas es el espacio que va a ver entre cada elemento
def armas(nombre,categoria,rareza):
    '''
        str,str,str-->dict
        OBJ:Almacenar datos de las armas en un diccionario
    '''
    return {'nombre':nombre, 'categoria':categoria, 'rareza':rareza}




def menor(rareza1,rareza2): #Esto lo puedo hacer con lo que sea para determinar el orden
    '''
        str,str-->bool
        OBJ:Determinar cual es la rareza menor
    '''
    orden = ('Comun', 'Poco_comun', 'Rara', 'Epica', 'Legendaria')

    return orden.index(rareza1) <= orden.index(rareza2)

def ordenar_burbuja(lista):
    '''
        list-->none
        OBJ:Recibe unos parametros en este caso la rareza y la devuelve ordenada
    '''
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if menor(lista[i]['rareza'],lista[j]['rareza']):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


mochila = []
arma1 = armas('ak-47','fusil de asalto','Rara')
arma2 = armas('snipper','lanzador','Epica')
arma3 = armas('Spash','Escopeta','Legendaria')
arma4 = armas('diggel','Pistola Pesada','Poco_comun')
arma5 = armas('Fusil de tambor','Ametralladora ligera','Comun')
mochila.append(arma1)
mochila.append(arma2)
mochila.append(arma3)
mochila.append(arma4)
mochila.append(arma5)


print('original:')
for arma in mochila:
    print(arma)
ordenar_burbuja(mochila)
print('ordenada:')
for arma in mochila:
    print(arma)

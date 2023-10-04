def inventario_ferreteria(codigo,producto,precio,stock):
    '''
        str,str,float,int-->dict
        OBJ:Crear un diccionario del inventario de una ferrreteria
    '''
    return {'codigo': codigo, 'producto': producto, 'precio': precio, 'stock': stock}

def menor(stock,stock2):
    '''
        list-->bool
        OBJ: Determinar el orden por stock
    '''
    orden = (10,8,5)
    return orden.index(stock)<= orden.index(stock2)
def ordenar(lista_datos):
    '''
        list-->None
        OBJ:Imprimir el inventario de la ferreteria de acuerdo al orden del stock
    '''
    for i in range(len(lista_datos)):
        for j in range(i+1,len(lista_datos)):
            if menor(lista_datos[i]['stock'],lista_datos[j]['stock']):
                aux = lista_datos[i]
                lista_datos[i] = lista_datos[j]
                lista_datos[j]= aux

#Probador
lista_datos = []
destornillador = inventario_ferreteria('REF_01','Destornillador', 12.50, 10)
taladro = inventario_ferreteria('REF_02', 'Taladro', 89.00, 5)
radial = inventario_ferreteria('REF_03', 'Radial', 150.00, 8)
LLave_inglesa = inventario_ferreteria('REF_04', 'LLave inglesa', 9.50, 10)
lista_datos.append(destornillador)
lista_datos.append(taladro)
lista_datos.append(radial)
lista_datos.append(LLave_inglesa)

ordenar(lista_datos)
print('Lista ordenada')
for i in lista_datos:
    print(i)
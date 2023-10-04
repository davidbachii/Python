import random
def mascarillas(modelo,tipo,color,precio,unidades):
    '''
        int,str,str,float,int-->dict
        OBJ:
    '''
    return {'modelo': modelo, 'tipo': tipo, 'color': color, 'precio': precio, 'unidades':unidades}

lista_mascarillas = []
for i in range(50):
    lista_mascarillas.append(mascarillas(random.randint(1000,2000),random.choice(['FFP1','FFP2','FFP3']),random.choice(['negro','blanco','multicolor']),
    random.uniform(0.30,0.80),random.randint(90,110)))
print(lista_mascarillas)


def stock_disponible(tipo,lista):
    '''
        str,list-->none
    '''
    lista_stock = []
    unidades = 0
    for i in lista:
        if i['tipo'] == tipo:
            print(f'Modelo {i["modelo"]}, precio {i["precio"]}€,  con {i["unidades"]} unidades')
            lista_stock += [i]
            unidades += i["unidades"]
    print(f'Unidades totales de mascrilla tipo {tipo}:{unidades}')


#print(stock_disponible('FFP2',lista_mascarillas))

def compra_mascarillas(tipo,unidades,lista):
    '''
        str,int,list-->None
    '''
    lista_actual = [stock_disponible(tipo,lista)]
    print(lista_actual)
    n = int(input('Introduce el modelo que usted desee comprar: '))
    for i in lista:
        if n == i["modelo"]:
            print(f'Ha de pagar {i["precio"] * unidades} € y quedan {i["unidades"] - unidades} unidades')
            if i["unidades"] < unidades:
                print('No se realizo la venta')
#print(compra_mascarillas('FFP2',80,lista_mascarillas))

def reponer(lista):
    lista_reponer = []
    for i in lista:
        if i['unidades'] < 100:
            lista_reponer.append(i['modelo'])
    return lista_reponer

print(reponer(lista_mascarillas))




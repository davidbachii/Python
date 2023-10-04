import random
def mascarillas(modelo,tipo,color,precio,unidades_disponibles):
    '''
        int,str,str,float,int-->dict
        OBJ: Crear un diccionario con los datos almacenados de las mascarillas
    '''
    return {'modelo': modelo, 'tipo': tipo, 'color': color, 'precio': precio, 'unidades': unidades_disponibles}

def mostrar_stock_por_tipo(tipo,lista_mascarillas):
    '''
        list-->none
    '''
    total_unidades = 0
    for i in lista_mascarillas:
        if i["tipo"] == tipo: #Si pongo FFP2 , me recorre mi lista de mascarillas y si encuentra una FFP2, me muestra el modelo
            #y las unidades disponibles
            print(f'Modelo: {i["modelo"]},{i["unidades"]} unidades')
            total_unidades += i["unidades"]
    print(f"Unidades totales de mascarilla de tipo:{tipo}:{total_unidades}")

def venta_mascarillas(tipo,lista_mascarillas,unidades):
    '''
        OBJ: Realiza una venta y actualiza stock de un tipo de mascarilla
    '''
    unidades_disponibles = 0
    contador = 0
    seguir = True
    print('Mascarillas disponibles......')
    for i in lista_mascarillas:
        if i["tipo"] == tipo and i["unidades"] > unidades:
            print(f'{contador}:{i["modelo"]},{i["precio"]} €')
            unidades_disponibles += i["unidades"]
            contador += 1
    modelo_elegir = input('Escoja un modelo:')
    for i in lista_mascarillas:
        if modelo_elegir == i['modelo']:
            i["unidades"] -= unidades
            precio = unidades * i["precio"]
            print(f'Total a pagar: {precio}')
            print('La compra se ha realizado con éxito')


def mascarillas_a_reponer(lista_mascarillas):
    '''
        list-->list
        OBJ:Retorna una lista con las mascarillas que se deben de reponer
    '''
    lista = []
    for i in lista_mascarillas:
        if i['unidades'] < 100:
            lista.append(i['modelo'])
    return lista




lista_mascarillas = []
for i in range(50):
    mascarilla = mascarillas(str(random.randint(1000,2000)),random.choice(['FFP1', 'FFP2','FFP3']),random.choice(['blanco','rojo','multicolor']),random.uniform(0.30,0.80),random.randint(90,100))
    lista_mascarillas.append(mascarilla)
#print(mostrar_stock_por_tipo('FFP2',lista_mascarillas))
print(venta_mascarillas('FFP2',lista_mascarillas,80))
#print(lista_mascarillas)
#print(mascarillas_a_reponer(lista_mascarillas))
print(lista_mascarillas)
modelo = input('introduce un modelo')
for i in lista_mascarillas:
    if modelo == i['modelo']:
        print(i)
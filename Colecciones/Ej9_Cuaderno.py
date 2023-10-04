'''
Piensa en las estructuras de datos que permitan almacenar información sobre personas
con objeto de hacer un estudio estadístico. Así, se deberá almacenar el nombre, sexo y
edad de cada persona. Programa posteriormente una función para leer por teclado
datos relativos a una persona y otra que muestra dichos datos por pantalla.
'''

def datos_persona(nombre,sexo,edad):
    '''
        str,str,int --> dict
        OBJ:Almacenar los datos de una persona
    '''
    return {'nombre': nombre, 'sexo': sexo, 'edad': edad}

def leer_datos():
    '''
        none-->dict
        OBJ: Leer datos de una persona y almacenrlos en un diccionario
    '''
    nombre = input("Introduce el nombre: ")
    sexo = input("Introduce el sexo (M o F):")
    seguir = True
    while seguir:
        try:
            edad = int(input("Introduce la edad"))
            seguir = False
        except:
            print("Edad mal introducida")
            seguir = True

    return datos_persona(nombre,sexo,edad)

def datos_por_pantalla(persona): #Esto recibe una persona y le imprime sus datos
    """
        dict-->none
        OBJ:Imprime los datos de la persona
    """
    print(f'Nombre: {persona["nombre"]}')  #de personas me imprime el nombre
    print(f'Edad: {persona["edad"]}')
    print(f'Sexo: {persona["sexo"]}')

'''
Programa un software que utilice lo programado en el ejercicio 1 para leer los datos de
10 personas y calcule la media de edad general, la media por sexo, la cantidad de
mujeres que tienen entre 13 y 16 años y el número de hombres menores de 20 años.
'''

def imprimir_lista_personas(lista_personas):
    '''
        list-->none
        OBJ:Imprimir una lista de personas reutilizando la funcion inicial
    '''
    print(f'Hay {len(lista_personas)} personas en la lista')
    persona = []
    for i in lista_personas:
        persona += [i]
    datos_por_pantalla(persona)
def calculo_media(lista_personas):
    '''
        list-->int
        OBJ: Calcular la media de edad
    '''
    suma = 0
    for i in lista_personas:
        suma += i["edad"]
    media = suma/len(lista_personas)
    return media

def busqueda_hombres(lista_personas):
    '''
        list-->list
    '''
    lista_Hombres = []
    for i in lista_personas:
        if i["sexo"] == 'm' or i["sexo"] == 'M':
            lista_Hombres.append(i)
    return lista_Hombres

def busqueda_mujeres(lista_personas):
    '''
        list-->list
        OBJ: Dada una lista de personas devolver una lista de las mujeres
    '''
    lista_mujeres = []
    for i in lista_personas:
        if i["sexo"] == 'F' or i["sexo"]== 'f':
            lista_mujeres.append(i)
    return lista_mujeres

def calcula_media_sexo(lista_personas):
    """
        list-->
        OBJ:imprime la media de edad por sexo
    """
    lista_hombres = busqueda_hombres(lista_personas)
    if len(lista_hombres) > 0:
        media_hombres = calculo_media(lista_hombres)
        print(f'la media de hombres es: {media_hombres}')
    else:
        print("No hay datos de hombres en la lista")
    lista_mujeres = busqueda_mujeres(lista_personas)
    if len(lista_mujeres) > 0:
        media_mujeres =calculo_media(lista_mujeres)
        print(f'La media de mujeres es: {media_mujeres}')
    else:
        print("No hay datos de mujeres en la lista")

def calculo_mujeres_13_16(lista_personas):
    '''
        list-->none
        OBJ:Imprime el numero de mujeres entre 13 y 16 años
    '''
    mujeres13_16 = 0
    for i in lista_personas:
        if 13 <= i["edad"] <= 16 and i["sexo"] == 'f':
            mujeres13_16 += 1
    print(f'El numero de mujeres entre 13 y 16: {mujeres13_16}')

def calculo_hombres_menores20(lista_personas):
    '''
        list-->none
        OBJ:Imprime los hombres menores de 20 años
    '''
    lista_hombres = busqueda_hombres(lista_personas)
    hombres_20 = 0
    for i in lista_hombres:
        if i["edad"]<= 20:
            hombres_20 +=1
    print(f'El numero de hombres menores de 20: {hombres_20}')

def busqueda_hombre_mas_joven(lista_personas):
    '''
        list-->none
        OBJ:Buscar el hombre mas joven
    '''
    lista_hombres = busqueda_hombres(lista_personas)
    person_mas_joven = lista_hombres[0] #Es como buscar el menor de una lista
    persona_mas_mayor = lista_hombres[0]
    if len(lista_hombres)>0:
        for i in lista_hombres:
            if i["edad"] < person_mas_joven["edad"]:
                person_mas_joven = i
            elif i["edad"] > persona_mas_mayor["edad"]:
                persona_mas_mayor = i

#Programa principal

lista_personas = []
opcion = 1
while opcion != 0:
    print('--------------------------------------------')
    print('------Gestion-de-personas-----------------')
    print('--------------------------------------------')
    print('1.- Introduce una persona.')
    print('2.- Muestra los datos de todas las personas.')
    print('3.- Calcula la media de edad de las personas introducidas')
    print('4.- Calcula la media de edad por sexo')
    print('5.- Calcula el número de mujeres entre 13 y 16 años')
    print('6.- Calcula el número de hombres menores de 20 años')
    print('7.- Muestra los datos del hombre más joven')
    print()
    print('0.- Salir')
    print('-----------------------------------------------')
    try:
        int(input('Seleccione una opcion: '))
    except:
        print('El valor introducido no es correcto')
    else:
        if 1<= opcion <=7:
            if opcion == 1:
              persona_nueva =  leer_datos()
              lista_personas.append(persona_nueva)
            elif opcion == 2:
                imprimir_lista_personas(lista_personas)
            elif opcion == 3:
                calculo_media(lista_personas)
            elif opcion == 4:
                calcula_media_sexo(lista_personas)
            elif opcion == 5:
                calculo_mujeres_13_16(lista_personas)
            elif opcion == 6:
                calculo_hombres_menores20(lista_personas)
            elif opcion == 7:
                busqueda_hombre_mas_joven(lista_personas)
        else:
            print('Opcion no existente')
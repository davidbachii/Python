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

def persona(nombre,sexo,edad):
    '''
        str,str,int-->dict
        OBJ: Almacenar los datos de una persona en un diccionario
    '''
    return {'nombre': nombre, 'sexo': sexo, 'edad': edad}
def leer_datos():
    '''
        none-->dict
        OBJ: Leer y alamcenar los datos introducidos en un diccionario
    '''
    nombre = input('Introduzca el nombre:')
    seguir = True
    while seguir:
        sexo = input('Introduce el sexo(m/f):')
        if sexo == 'm' or sexo == 'f':
            seguir = False
        else:
            print('Sexo no existente')
            seguir = True
    edad = int(input('Introduce la edad: '))
    return persona(nombre,sexo,edad)

def mostrar_datos_persona(persona):
    '''
        persona-->none
        OBJ: Poder ver los datos de una persona
    '''
    print(f'El nombre es {persona["nombre"]}')
    print(f'La edad es {persona["edad"]} años')
    print(f'El sexo es {persona["sexo"]}')
def mostrar_datos_personas(lista_personas):
    '''
        list-->list

    '''
    for i in lista_personas:
        print(f'El nombre es {i["nombre"]}')
        print(f'La edad es {i["edad"]} años')
        print(f'El sexo es {i["sexo"]}')





lista_personas = []
for i in range(2):
    lista_personas.append(leer_datos())
persona1 = persona('David','m',22)
lista_personas.append(persona1)
print(mostrar_datos_persona(persona1))
print(mostrar_datos_personas(lista_personas))

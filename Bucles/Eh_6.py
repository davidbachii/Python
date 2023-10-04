'''
Programa un procedimiento que dibuje en pantalla un rectángulo de dimensiones
dadas con un símbolo que se le especifica. Por ejemplo, la llamada al
procedimiento dibujar_rectangulo(3,5,’#’) produciría la siguiente salida:
'''

def dibijar_rectangulo(a,b,icon):
    '''
        int,int,none-->none
        OBJ:Dibujar un rectangulo de 3*5 con #
    '''

    for i in range(a):
        for j in range(b):
            print(icon,end=" ")
        print()


#Probadores
print(dibijar_rectangulo(3,5,"#"))

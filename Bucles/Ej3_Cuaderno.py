'''
Implementa una variante del Ejercicio Resuelto 3 que dibuje en pantalla un
rectángulo de dimensiones dadas pero con dos símbolos, las filas pares con ‘@’ y
las impares con ‘#’. Esta será la versión “3a”. Después de hacerlo, crea una
segunda versión “3b” para que esta vez los símbolos se alternen en las columnas,
es decir, las columnas pares se dibujarán con ‘@’ y las impares con ‘#’
'''
#3b
for i in range(3):
    for j in range(5):
        print("#","@",end=" ")
    print()
print()
print()
#3a
#Para yo saber si mi columna es par o no tengo que definir una funcion
def es_par(num):
    '''
        int-->boll
        OBJ: Detectar si es par o no
    '''
    return num % 2 == 0

for i in range(3):
    for j in range(5):
        if es_par(i):
            print("#", end=" ")
        else:
            print("@",end=" ")
    print()
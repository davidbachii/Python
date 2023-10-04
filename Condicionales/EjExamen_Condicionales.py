'''
Se desea implementar un programa en Python que simule el comportamiento de una máquina
tragaperras. Para ello vamos a seguir los siguientes pasos:
1. Programa la función tirada que no recibe ningún parámetro y devuelve 3 números
aleatorios entre 1 y 6 (incluidos). Utiliza la función random.randint(min,max) para
generar los números. (1.5 puntos)
2. Programa la función premio que recibe 3 números enteros y devuelve las monedas que
ha ganado el jugador en una tirada. El jugador gana 5 monedas si los 3 números son
iguales y 2 monedas si han salido 2 números iguales, en otro caso no gana ninguna
moneda. (1.5 puntos)
3. Implementa el programa principal: El número de monedas iniciales se define como una
constante (por ejemplo 3). Mientras el número de monedas sea mayor que 0 y el usuario
quiera seguir jugando, se generará una tirada y se comprobará el premio (usando las
funciones de los apartados 1 y 2). Al final de cada tirada se le restará una moneda y se
preguntará si quiere seguir jugando. El programa principal imprimirá por pantalla los
siguientes mensajes: (2 puntos)
Empieza la partida con 3 moneda(s).
Tirada: 3 3 1
Ha ganado 2 monedas. Ahora tiene 4 monedas.
¿Quiere seguir jugando? (s/n): s
Tirada: 6 6 6
Ha ganado 5 monedas. Ahora tiene 8 monedas.
¿Quiere seguir jugando? (s/n): n
Ha acabado la partida con 8 moneda(s).
'''
import random

def tirada():
    '''
        none-->int,int,int
        OBJ: Devolver tres numeros aleatorios entre el uno y el seis
    '''
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    n3 = random.randint(1, 6)
    return n1, n2, n3


def premio(n1, n2, n3):
    '''
        int,int,int-->int
        OBJ:Devolver las monedas que ha ganado el jugador en una tirada
    '''
    if n1 == n2 == n3:
        monedas = 5
    elif n1 == n2 or n2 == n3 or n1 == n3:
        monedas = 2
    elif n1 != n2 or n1!= n2 or n2 != n3:
        monedas = 0
    return monedas


#Probadores
monedas_iniciales = 3

seguir = True
monedas = monedas_iniciales
print(f"Empieza la partida con {monedas} monedas")
while monedas > 0 and seguir:
    t1, t2, t3 = tirada()
    print(f"Tirada: {t1}, {t2}, {t3}")
    monedas_ganadas = premio(t1, t2, t3)
    monedas += monedas_ganadas -1
    print(f"Ha ganado {monedas_ganadas} monedas, usted posee {monedas} monedas")
    if monedas > 0:
        jugar = input("¿Quiere seguir jugando?(s/n):")
        if jugar == 'n':
            seguir = False
print(f"Ha acabado la partida con {monedas} monedas, recuerda que el banco siempre gana")



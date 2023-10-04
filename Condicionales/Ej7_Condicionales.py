def ptos_niño(ingresos):
    '''
        int-->int
        OBJ: Calcular los puntos del ninño-niña segun sus ingresos
        PRE: ingresos > 0
    '''

    if ingresos >= 5000:
        ptos = 1
        print(f"Ha obtenido {ptos} puntos")
    elif 3500 <= ingresos < 5000:
        ptos = 2
        print(f"Ha obtenido {ptos} puntos")
    elif 1800 <= ingresos < 3500:
        ptos = 3
        print(f"Ha obtenido {ptos} puntos")
    else:
        ptos = 4
        print(f"Ha obtenido {ptos} puntos")
    return ptos






#Probador
try:
    ingresos = int(input("Introduzca los ingresos ganados: "))
    print(f"Los puntos que le corresponden a su familia son {ptos_niño(ingresos)} ")
except:
    print("Dato introducido no valido")
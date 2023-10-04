
def es_cadena_binaria(cadena):
    '''
        string --> boll
        OBJ: Saber si nuestra cadena es binaria o o no
    '''
    for i in cadena:
        if i =='1' or i =='0' and len(cadena) == 7:
            es_cadena = True

        else:
            es_cadena = False

    if es_cadena == True:
        print("Es una cadena binaria")
    elif es_cadena == False:
        print("No es cadena binaria")


    return es_cadena

def leer_cadena_binaria():
    seguir = True

    while seguir:
        try:
            cadena = input("Introduce una cadena binaria: ")
        except:
            print("El valor introducido no es una cadena")
            seguir = True
        else:
            if len(cadena) != 7:
                seguir = True
            else:
                if len(cadena) == 7:
                    seguir = False
    return cadena

def tiene_pariedad_par(cadena):
    contador = 0
    for i in cadena:
        if i == '1':
            contador += 1
        if contador % 2 == 0:
            es_pariedad_par = True
        else:
            es_pariedad_par = False
    return es_pariedad_par


#Probador
cadena = leer_cadena_binaria()
print(es_cadena_binaria(cadena))
print(tiene_pariedad_par(cadena))



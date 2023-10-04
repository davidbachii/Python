#Pedir por pantalla un numero y sacar su tabla de multipicar
seguir = True
while seguir:
    try:
        numero = int(input("Introduzca un numero entero: "))
        seguir = False
    except:
        print("El valor introducido no es un numero entero")
    else:
        print(f"Tbla del {numero}")
        for i in range(1,11): #Recorre desde el numero uno hasta  el numero 10 , los de la tabla de multiplicar en este caso

                print(f"{i} * {numero} = {i*numero}")
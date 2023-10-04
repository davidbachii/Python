#Hay que pedirle al usuario una serie de numeros enteros y clasificarlos en pares e impares
seguir = True
contador = 0
pares = 0
impares = 0
nulos = 0

while seguir:
    try:

        n = int(input("Ingrese la cantidad de datos que desea clasificar: "))
        seguir = False
    except:
        print("Dato intoducido erronemente, vuelvslo a introducir")
        seguir = True

for i in range (n):
    numero =print(int(input(f"introduzca el numero {contador+1}: ")))
    contador +=1

    if numero % 2 == 0:
        pares +=1
    elif numero % 2 != 0:
        impares += 1
    else:
        nulos +=1

print(f"Numeros pares totales:{pares}\n"
      f"Numeros impares totales{impares}\n"
      f"Numros nulos totlaes{nulos}")



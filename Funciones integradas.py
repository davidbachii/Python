#Funciones integradas

#Pasar de una cadena a un entero

n = int("10")
print(n)

n = float("5.9")
print(n)

#Pasar de un entero a una cadena

n = str("12.5")
print(n)

#Pasar un numero entero a binario o hexadecimal y viceversa

n = bin(10)
print(n)  #Convertir el numero a binario un detalle al ejecutarlo es que el numero sale 0b y luego ya el numero en binario en este caso 1010
n = hex(10)
print(n) #Lo mismo me sale 0x y el numero en hexadecimal

n = int("0b1001",2) #Base dos para que se sepa que es binario
print(n)
n = int("0xa",16) #Base dieciseis para que se sepa que es hexadecimal
print(n)

#Otras funciones
n = round(5.7) # Redonde el numero a la cifra entera mas cercana  
print(n)
n = len("David") #Saca la longitud de la cadena establecida en este caso 5
print(n)
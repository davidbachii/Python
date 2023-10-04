saldo = 1000
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero")
print("4. Salir")
operacion = int(input("Introduzca la operacion de desea realizar: "))

if operacion == 1:
    ingresar = int(input("¿Cuanto dinero desea ingresar: "))
    dinero_final = saldo + ingresar
    print(f"Usted dispone de {dinero_final}€")
elif operacion == 2:
        ingresar = int(input("¿Cuanto dinero desea retirar: "))
        dinero_final = saldo - ingresar
        if ingresar>saldo:
            print("Usted no dispone de ese dinero ")
            print(f"Usted dispone de {dinero_final}€")

elif operacion == 3:
    print(f"Su saldo actual es de {saldo}")
elif operacion == 4:
    print("Gracias por confiar en nosotros que pase un buen dia caballero")
else:
    print("Operacion erronea intriduzcala correctamente")
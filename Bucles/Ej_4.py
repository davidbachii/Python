#Un programa que pida los datos de hombres y mujeres y calcule su promedio de edad
seguir = True
peso_hombres = 0
peso_mujeres = 0
altura_hombres = 0
altura_mujeres = 0
cantidad_hombres = 0
cantidad_mujeres = 0

while seguir:
    try:
        numero = int(input("Introduce el numero de personas a analizar: "))
        seguir = False
    except:
        print("El valor introducido no es correcto, introduzcalo de nuevo")
        seguir = True


for i in range (numero):
    peso  =  (int(input("Introduzca el peso en kg: ")))
    altura = (float(input("Introduzca la altura en centimetros: ")))
    genero = (input("Seleccione el genero (M) o (F):"))

    if genero== 'm' or genero == 'M':
        peso_hombres += peso
        altura_hombres += altura
        cantidad_hombres+=1
    elif genero == 'f' or genero == 'F':
        peso_mujeres += peso
        altura_mujeres += altura
        cantidad_mujeres += 1

        promedio_pesoH = peso_hombres/cantidad_hombres
        promedio_pesoM = peso_mujeres/cantidad_mujeres
        promedio_alturaH = altura_hombres/cantidad_hombres
        promedio_alturaM = altura_mujeres/cantidad_mujeres

print(f"De los promedios recogidos"
        f"\n El promedio de peso de los hombres es: {promedio_pesoH}"
        f"\n de las mujeres: {promedio_pesoM}"
        f"\n El promedio de altura de los hombres es: {promedio_alturaH}"
        f"\n y de las mujeres : {promedio_alturaM} ")


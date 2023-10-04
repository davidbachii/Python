notas = ('3', '4', '5', '7', '9')
calificaciones = ('supenso', 'suspenso', 'suficinete', 'notable', 'sobresaliente')

nota_final = ''
for i in notas:

    if i in notas:
        nota_final += calificaciones[notas.index(i)]
    else:
        nota_final += i

print(nota_final)
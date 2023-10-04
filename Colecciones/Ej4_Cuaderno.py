'''
Implemente una función que indique si una palabra contiene las cinco
vocales: por ejemplo “murciélago”. Modifique posteriormente la función para
que detecte sólo aquellas palabras que contienen una única vez cada vocal.
'''
vocales = []
variable = 0
palabra = input("Introduce una palabra: ")
for i in palabra:
    if i == 'a' or i =='e' or i == 'i' or i =='o' or i =='u':
        vocales += [i]
    for i in vocales:
        if i =='a' and i == 'e' and i == 'i' and i == 'o' and i == 'u':
            variable = True
        else:
            variable = False

print(vocales)
print(variable)
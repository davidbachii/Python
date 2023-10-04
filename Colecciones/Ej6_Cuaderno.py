'''
Escriba un programa que “codifique” una frase modificando todas las vocales
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el
símbolo #. Por ejemplo, la frase: “Un perro del hortelano”, deberá
devolverse: “#n p3rr0 d3l h0rt3l4n0”.
'''


vocales = ('a','e','i','o','u')
codigos = ('4','3','2','1','#')

cadena = input("Introduce una cadena: ")
resultado = ''

for i in cadena:
    minisculas = i.lower()
    if minisculas in vocales:
        resultado += codigos[vocales.index(minisculas)]
    else:
        resultado += i
print(resultado)








'''
Operaciones logicas
and:

TRUE&TRUE-->TRUE
TRUE&FALSE-->FALSE
FALSE&TRUE-->FALSE
FALSE&FALSE-->TRUE

or:

TRUE&TRUE-->TRUE
TRUE&FALSE-->TRUE
FALSE&TRUE-->TRUE
FALSE&FALSE-->FALSE
'''

a=10
b=12
c=13
d=10

resultado = ((a>b)or(a<c)and(a==c)or(a>=b))
#False or True and False or False
#True and False
#False

print(resultado)
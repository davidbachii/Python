#3 comprobacion mcd,mcm
"""
sage: gcd(266,181)
1
sage: lcm(266,181)
48146
sage: gcd(72566,17662) (maximo comun divisor)
2
sage: lcm(72566,17662) (minimo comun multiplo)
640830346
"""



#1
sage: (373//52)
7
sage: (373%52)
9
sage: (-373//52)
-8
sage: (-373%52)
43

#2
"""
sage: def algoritmo1(a,b):
....:     q = 0
....:     r = a
....:     while r>= b:
....:         r = r-b
....:         q += 1
....:     if a < 0 and r >= 0:
....:         r = b-r
....:         q = -(q + 1)
....:     return q,r
....:
....:
sage: algoritmo1(373,52)
(7, 9)
"""

#3
"""
sage: time(373//52)
CPU times: user 0 ns, sys: 0 ns, total: 0 ns
Wall time: 825 µs
7
sage: time(373%52)
CPU times: user 0 ns, sys: 0 ns, total: 0 ns
Wall time: 28.1 µs
9

sage: time(algoritmo1(373,52))
CPU times: user 0 ns, sys: 0 ns, total: 0 ns
Wall time: 34.8 µs
(7, 9)
"""




a = "hola"
b = "que tal"

print(f"{a}Juan{b}")


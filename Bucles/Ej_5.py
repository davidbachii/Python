n = 5

for i in range(1,n+1):
    for j in range(i): #Como es range i y rango de i es 6,empieza con el uno y lee 0, luego con el 2 y ya lee uno,con el 3 lee 2,etc
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print()
print()

for i in[1, 2, 3]:
    for j in range(i):
        print(f"i vale {i} y j vale {j}")
""" __author__: Leynilson José "Snake" """
# Pares e | accepted


t = int(input())

pares = []
impares = []

for i in range(t):
    numero = input()
    if int(numero[-1]) % 2 == 0:
        pares.append(int(numero))
    else:
        impares.append(int(numero))

pares.sort()
impares.sort(reverse=True)

for p in pares:
    print(p)
for i in impares:
    print(i)

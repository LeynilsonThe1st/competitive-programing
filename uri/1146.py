""" __author__: Leynilson José "Snake" """
# Sequências Crescentes

t = int(input())

while t != 0:
    for i in range(t):
        if i == t-1:
            print(i+1)
        else:
            print(i+1, end="->")

    t = int(input())
    if t == 0:
        break


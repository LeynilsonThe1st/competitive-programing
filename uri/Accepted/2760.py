""" __author__: Leynilson José "Snake" """
# Entrada e saida de strings | accepted

a = input()
b = input()
c = input()

print(f"{a}{b}{c}")
print(f"{b}{c}{a}")
print(f"{c}{a}{b}")
print(f"{a[:10]}{b[:10]}{c[:10]}")

""" __author__: Leynilson José "Snake" """
# Cifra de cesar | accepted


def getLetra(s: str, n: int):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    si = letras.index(s)
    return letras[si - n]


def makeString(s: str, n: int):
    return ''.join([getLetra(x, n) for x in s])


t = int(input())
while t > 0:
    t -= 1
    palavra = input()
    posi = int(input())

    if posi == 0:
        print(palavra)
    else:
        print(makeString(palavra, posi))

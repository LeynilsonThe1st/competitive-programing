""" __author__: Leynilson José "Snake" """
# Frequencia de letras | accepted


def countChar(string: list):
    freq = []
    while len(string) > 0:
        char = string[0]
        if char.isalpha():
            freq.append((string.count(char), char))
        string = list(filter(lambda x: x != char, string))
    return freq


def ordenar(arr: list):
    out = []
    maior = max(arr)
    freq, letra = maior
    out.append(letra)
    arr.remove(maior)
    while len(arr) > 0:
        fq, lt = max(arr)
        arr.remove((fq, lt))
        if fq == freq:
            out.append(lt)
    out.sort()
    return "".join(out)


t = int(input())
while t > 0:
    t -= 1
    frase = list(input().lower())
    print(ordenar(countChar(frase)))

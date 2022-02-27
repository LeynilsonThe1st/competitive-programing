""" __author__: Leynilson José "Snake" """
# Sobrenome Não é Fácil

CONS = 'BCDFGHJKLMNPQRSTVWXYZ'

t = int(input())
while t > 0:
    t -= 1

    original = snome = input()
    snome = snome.upper()

    tamanho = len(snome)

    if tamanho < 3:
        print(original, 'eh facil')

    else:
        i = 0
        while i < tamanho:
            if i < tamanho - 2 and snome[i] in CONS and snome[i+1] in CONS and snome[i+2] in CONS:
                print(original, 'nao eh facil')
                break

            # ultimo loop
            elif i == tamanho - 1:
                print(original, 'eh facil')
            i += 1

""" __author__: Leynilson José "Snake" """
# Mensagem oculta | accepted


t = int(input())
for _ in range(t):
    print(''.join(map(lambda x: x[0], input().split())))

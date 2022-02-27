""" __author__: Leynilson José "Snake" """
# Juros do projecto | accepted


def cin():
    try:
        global x, y
        x, y = map(float, input().split())
        return True
    except EOFError:
        return False


x = y = None
i = 1
while cin():
    z = ((y / x) - 1) * 100
    print(f"Projeto: {i}:")
    print(f"Percentual dos juros da aplicacao: \n{z:.2f} %\n")
    i += 1

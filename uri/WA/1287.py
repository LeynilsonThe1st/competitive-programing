""" __author__: Leynilson José "Snake" """
# Processador amigavel de inteiros | wrong answer


def cin():
    try:
        global string
        string = input().strip(' ').replace(',', '').lower()
        string = string.replace('l', '1').replace('o', '0')
        return True
    except EOFError:
        return False


string = None
while cin():
    if len(string) > 0 and string.isnumeric():
        numero = int(string)
        if numero > 2147483647:
            print('error')
        else:
            print(numero)
    else:
        print('error')

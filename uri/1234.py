

def cin():
    try:
        global frase
        frase = input()
        return True
    except EOFError:
        return False

while cin():

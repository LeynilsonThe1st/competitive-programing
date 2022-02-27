class Node:
    def __init__(self, letra):
        self.esq = None
        self.dir = None
        self.letra = letra


def addNode(raiz: Node, novo_node):
    if not raiz.esq:
        raiz.esq = novo_node
    elif not raiz.dir:
        raiz.dir = novo_node


def infixo(raiz):
    if raiz:
        infixo(raiz.esq)
        print(raiz.letra, end=" ")
        infixo(raiz.dir)


def posfixo(raiz):
    if raiz:
        posfixo(raiz.esq)
        posfixo(raiz.dir)
        print(raiz.letra, end=" ")


def prefixo(raiz):
    if raiz:
        print(raiz.letra, end=" ")
        prefixo(raiz.esq)
        prefixo(raiz.dir)


t = int(input())
while t > 0:
    t -= 1

    n, s1, s2 = input().split()

    root = Node(s1[0])
    s1 = s1[1:]
    for letra in s1:
        addNode(root, Node(letra))

    print("Preorder traversal of binary tree is")
    prefixo(root)

    print("\nInorder traversal of binary tree is")
    infixo(raiz)

    print("\nPostorder traversal of binary tree is")
    posfixo(raiz)
    print()


# raiz = Node('a')
# addNode(raiz, Node('b'))
# addNode(raiz, Node('c'))
# addNode(raiz, Node('d'))
# raiz.addNode(Node('e'))
# raiz.addNode(Node('f'))

# raiz.esq = Node('b')
# raiz.esq.esq = Node('c')
# raiz.dir = Node('d')
# raiz.dir.esq = Node('e')
# raiz.dir.dir = Node('f')

print("Preorder traversal of binary tree is")
prefixo(raiz)

print("\nInorder traversal of binary tree is")
infixo(raiz)

print("\nPostorder traversal of binary tree is")
posfixo(raiz)
print()

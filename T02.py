class BSTNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#          2
#        /  \
#       /    \
#     3        4
#    /  \     / \
#   5    6   7   8

    def ContarNodosInternos(self):
        if self.left is None and self.right is None:
            return 0
        else:
            lefnode = self.left.ContarNodosInternos() if self.left else 0
            rightnode = self.right.ContarNodosInternos() if self.right else 0
            return 1 + lefnode + rightnode

if __name__ == '__main__':
    NodoRoot = BSTNode(2)
    NodoRoot.left = BSTNode(3)
    NodoRoot.right = BSTNode(4)
    NodoRoot.left.left = BSTNode(5)
    NodoRoot.left.right = BSTNode(6)
    NodoRoot.right.left = BSTNode(7)
    NodoRoot.right.right = BSTNode(8)
    dato = NodoRoot.ContarNodosInternos()
    print("Numero de nodos: ", dato)
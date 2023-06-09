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

    def DistanciaNodo(self,data):
        if self.data == data:
            return 0
        elif data < self.data and self.left is not None:
            return 1 + self.left.DistanciaNodo(data)
        elif data > self.data and self.right is not None:
            return 1 + self.right.DistanciaNodo(data)
        else:
            return float('inf')

if __name__ == '__main__':
    NodoRoot = BSTNode(2)
    NodoRoot.left = BSTNode(3)
    NodoRoot.right = BSTNode(4)
    NodoRoot.left.left = BSTNode(5)
    NodoRoot.left.right = BSTNode(6)
    NodoRoot.right.left = BSTNode(7)
    NodoRoot.right.right = BSTNode(8)

    nododato = 8
    dato = NodoRoot.DistanciaNodo(nododato)
    print(f"la distacia al nodo {nododato} es: ", dato)

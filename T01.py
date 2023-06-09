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

    def ContarHojas(self):
        if self.left is None and self.right is None:
            return 1
        else:
            lefhojas = self.left.ContarHojas() if self.left else 0
            righthojas = self.right.ContarHojas() if self.right else 0
            return lefhojas + righthojas

if __name__ == '__main__':
    NodoRoot = BSTNode(2)
    NodoRoot.left = BSTNode(3)
    NodoRoot.right = BSTNode(4)
    NodoRoot.left.left = BSTNode(5)
    NodoRoot.left.right = BSTNode(6)
    NodoRoot.right.left = BSTNode(7)
    NodoRoot.right.right = BSTNode(8)
    dato = NodoRoot.ContarHojas()
    print("Numero de Hojas: ", dato)
class BSTNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def Equilibrado(self):
        return self.ComprobarEquilibrio() != -1

    def ComprobarEquilibrio(self):
        if self is None:
            return 0

        leftaltura = self.left.ComprobarEquilibrio() if self.left else 0
        rightaltura = self.right.ComprobarEquilibrio() if self.right else 0

        if leftaltura == -1 or rightaltura == -1 or abs(leftaltura - rightaltura) > 1:
            return -1

        return max(leftaltura, rightaltura) +1

#          2
#        /  \
#       /    \
#     3        4
#    /  \     / \
#   5    6   7   8

if __name__ == '__main__':
    NodoRoot = BSTNode(2)
    NodoRoot.left = BSTNode(3)
    NodoRoot.right = BSTNode(4)
    NodoRoot.left.left = BSTNode(5)
    NodoRoot.left.right = BSTNode(6)
    NodoRoot.right.left = BSTNode(7)
    NodoRoot.right.right = BSTNode(8)

    dato = NodoRoot.Equilibrado()
    if dato:
        print("Arbol Equilibrado... :", dato)
    else:
        print("No esta Equilibrado")
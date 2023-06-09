class BSTNode:
    '''
    Node BST definition
    '''

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
#
#          2
#        /  \
#       /    \
#     3        4
#    /  \     / \
#   5    6   7   8
#
def find(root, data):
    '''
    Method to find data in BST
    Rparam root:
    :return:
    '''
    currentNode = root

    if currentNode == None:
        return None
    else:
        if data == currentNode.data:
            return currentNode
        if data < currentNode.data:
            return find(currentNode.left, data)
        else:
            return find(currentNode.right, data)

if __name__ == '__main__':
    NodoRoot = BSTNode(2)
    NodoRoot.left = BSTNode(3)
    NodoRoot.right = BSTNode(4)
    NodoRoot.left.left = BSTNode(5)
    NodoRoot.left.right = BSTNode(6)
    NodoRoot.right.left = BSTNode(7)
    NodoRoot.right.right = BSTNode(8)
    dato = find(NodoRoot,2)
    print("Si se encontro el valor: ",dato.data)

import imp
modl = imp.load_source('binary_search_tree', '../week_4/binary_search_tree.py')
BST = modl.BST
class Node:
    def __init__(self, key, val, N=1, color="Black"):
        self.key = key
        self.val = val
        self.N = N
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree(BST):
    def _put(self, node, key, val):
        #base case
        if node == None:
            return Node(key, val, RED)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            # if equal, overwrite val
            node.val = val

        #RED-BLACK ROTATIONS
        if isRed(node.right) and not isRed(node.left):
            node = rotateLeft(node)
        if isRed(node.left) and isRed(node.left.left):
            node = rotateRight(node)
        if isRed(node.left) and isRed(node.right):
            flipColors(node)

        node.N = 1 + self._size(node.left) + self._size(node.right)
        return node

    def isRed(self, node):
        return node.color == "Red"

    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = "Red"
        return x

    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = "Red"
        return x

    def flipColors(self,node):
        node.color = "Red"
        node.left.color = "Black"
        node.left.color = "Red"

if __name__ == "__main__":
    bs = BST()
    bs.put(22, "A")
    bs.put(5, "B")
    bs.put(2, "B")
    bs.put(42, "C")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self._QueueIterator(self)

    class _QueueIterator:
        def __init__(self, queue):
            self._items = queue.items
            self._limit = queue.size()
            self._count = 1

        def hasNext(self):
            return self._count <= self._limit

        def next(self):
            if not self.hasNext():
                raise StopIteration

            item = self._items[self._limit - self._count]
            self._count += 1
            return item
class Node:
    def __init__(self, key, val, N=1):
        self.key = key
        self.val = val
        self.N = N
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node_x):
        return node_x.N if node_x is not None else 0

    def get(self, key):
        return self._get(self.root, key)

    # recursive private method
    def _get(self, key):
        x = self.root
        while x is not None:
            if key == x.key:
                return x.val
            if key < x.key:
                return self._get(x.left, key)
            else:
                return self._get(x.right, key)

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    # number of compares is equal to 1+depth of node
    def _put(self, start, key, val):
        #base case
        if start == None:
            return Node(key, val)
        if key < start.key:
            start.left = self._put(start.left, key, val)
        elif key > start.key:
            start.right = self._put(start.right, key, val)
        else:
            # if equal, overwrite val
            start.val = val
        start.N = 1 + self._size(start.left) + self._size(start.right)
        return start

    def get_min(self):
        x = self.root
        while x and x.left is not None:
            x = x.left
            return x.key

    def _get_min_node(self, node):
        return node if node.left is None else self._get_min_node(node.left)

    def get_max(self):
        x = self.root
        while x.right is not None:
            x = x.right
        return x.key
    # biggest key LESS than key given
    def floor(self, key):
        x = self._floor(self.root, key)
        return x.key if x is not None else None

    def _floor(self, x, key):
        if x is None:
            return None
        if key == x.key:
            return x
        elif key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        return t if t is not None else x

    def ceiling(self, key):
        x = self._ceiling(self.root, key) or None
        return x.key

    def _ceiling(self, x, key):
        if x is None:
            return None

        if key == x.key:
            return x
        elif key < x.key:
            t = self._ceiling(x.left, key)
            return t if t is not None else x
        return self._ceiling(x.right, key)

    # how many nodes < k?
    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, x):
        if x is None:
            return 0
        elif key < x.key:
            return self._rank(key, x.left)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(key, x.right)
        else:
            return self._size(x.left)

    def inorder_traversal(self):
        q = Queue()
        self._inorder(self.root, q)
        return q
    # yields keys in ascending order
    def _inorder(self,x, queue):
        if x is None:
            return
        self._inorder(x.left, queue)
        queue.enqueue(x.key)
        self._inorder(x.right, queue)

    def delete_min(self):
        root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        # if
        node.left = self._delete_min(node.left)
        node.N = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.N = 1 + self._size(node.left) + self._size(node.right)
        return node
    # hibbart delete
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, k):
        if node is None:
            return None
        if k < node.key:
            node.left = self._delete(node.left, k)
        elif k > node.key:
            node.right = self._delete(node.right, k)
        else:
            # if node only has one child, replace it with that child node
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            # if node has TWO children
            t = node
            # go to the right tree and get smallest child to uphold BST symmetry
            node = self._get_min_node(t.right)
            # make the right
            node.right = self._delete_min(t.right)
            node.left = t.left

        node.N = self._size(node.left) +  self._size(node.right) + 1
        return node

if __name__ == "__main__":
    bs = BST()
    bs.put(22, "A")
    bs.put(5, "B")
    bs.put(2, "B")
    bs.put(42, "C")
    print bs.size()
    print bs.get_min()
    print bs.get_max()
    print bs.floor(13)
    print bs.ceiling(1)
    print bs.rank(42)
    inorder = bs.inorder_traversal()
    for i in inorder:
        print i
    bs.delete_min()
    bs.delete_min()
    print bs.get_min()
    bs.delete_max()
    print bs.get_max()
    bs.delete(22)
    print bs.root.key

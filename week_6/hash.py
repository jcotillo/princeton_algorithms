import imp
modl = imp.load_source('LinkedList', '../week_1/linked_list.py')
LinkedList = modl.LinkedList

# Separate chaining hashing symbol table
class hashST:
    _CAPACITY = 4
    class Node:
        def __init__(self, key, val, next):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self, M=None):
        self.N = 0 # number of key-value pairs
        self.st = [LinkedList() for i in range(M)] #array of linked-list symbol table
        self.M = M or _CAPACITY # hash table size

    def _hash(self, node):
        # returns a value between 0 and M-1
        return (hash(key) & 0x7fffffffffffffff) % self.M
        # another possible hash function spotted on stack overflow:
        # return ord(node.val) + 101*self.M

    def constains(self, key):
        return self.st.get(key) is not None

    def get(self, key):
        i = self._hash(key)
        return self.st[i].search(key)

    def put(self, key, val):
        i = self._hash(key)
        self.st[i].search(key, val)

from sequential_search_st import SequentialSearchST

# Separate chaining hashing symbol table
class hashST:
    CAPACITY = 4
    class Node:
        def __init__(self, key, val, next):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self, M=None):
        self.N = 0 # number of key-value pairs
        self.M = M or self.CAPACITY # hash table size
        self.st = [SequentialSearchST() for i in range(self.M)] # array of linked-list symbol table

    def _hash(self, key):
        # returns a value between 0 and M-1
        return (hash(key) & 0x7ffffffffffffff) % self.M
        # another possible hash function spotted on stack overflow:
        # return ord(node.key) + 101*self.M

    def contains(self, key):
        return self.st.get(key) is not None

    def get(self, key):
        i = self._hash(key)
        #look at the correct hashed key for the this particular node
        return self.st[i].get(key)

    def put(self, key, val):
        i = self._hash(key)
        # only add to the total of nodes if it's a new node, not just with updated value
        if self.st[i].contains(key):
            self.N += 1
        self.st[i].put(key,val)

if __name__ == "__main__":
    st = hashST()
    st.put(12, "Monkey") # => i = 3
    st.put(10, "Pig") # =>
    st.put(20, "Rabbit") # => i = 3
    print st.get(42)
    st.put(1, "Elephant")
    print st.get(1)
    print st.N

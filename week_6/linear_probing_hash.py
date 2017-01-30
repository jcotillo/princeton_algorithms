class LinearProbingHash:
    CAPACITY = 4

    def __init__(self, cap=None):
        self.M = cap or self.CAPACITY
        self.N = 0
        self.values = [None for i in range(self.M)]
        self.keys = [None for i in range(self.M)]

    def _hash(self, key):
        # returns a value between 0 and M-1
        return (hash(key) & 0x7ffffffffffffff) % self.M
        # another possible hash function spotted on stack overflow:
        # return ord(node.key) + 101*self.M

    def _resize(self, capacity):
        temp = LinearProbingHash(capacity)
        for i in range(self.M):
            if self.keys[i] is not None:
                temp.put(self.keys[i], self.values[i])
        self.keys = temp.keys
        self.values = temp.values
        self.M = temp.M

    def put(self, key, value):
        # double table size if 50% full
        if self.N >= self.M/2:
            self._resize(2*self.M)

        i = self._hash(key)
        #look for empty slot or the same key to update it
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.values[i] = value
                return
            i = (i+1) % self.M

        self.keys[i] = key
        self.N += 1
        self.values[i] = value

    def get(self, key):
        i = self._hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.values[i]
            i = (i+1) % self.M
        return None

    # in delete method the array should resize down as well

if __name__ == "__main__":
    st = LinearProbingHash()
    st.put(12, "Monkey") # => i = 3
    st.put(10, "Pig") # =>
    st.put(20, "Rabbit") # => i = 3
    print st.get(42)
    st.put(10, "Elephant")
    print st.get(10)
    #should resize
    st.put(33, "Bird")
    st.put(25, "Chicken")
    st.put(75, "Snake")
    print st.values
    print st.keys

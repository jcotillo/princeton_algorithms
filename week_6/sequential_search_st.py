class SequentialSearchST:
    class Node:
        def __init__(self, key, val, next):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        self.N = 0 # total number of key-value pairs
        self.first = None #the head of the linkedList of key-value pairs

    def size(self):
        return self.N

    def isEmpty(self):
        return self.size() == 0

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        x = self.first
        while x is not None:
            if key is x.key:
                return x.val
            x = x.next
        return None # not in the linkedlist symbol table

    def put(self, key, val):
        # delete if val is None
        if val is None:
            self.delete(key)
            return

        # update value if key already in linkedlist
        x = self.first #from head to the end of the linkedlist
        while x is not None:
            if key == x.key:
                x.val = val
                return
            x = x.next

        # add new node if not in the list and value is present
        self.first = self.Node(key, val, self.first)
        self.N += 1

    def delete(self, key):
        self.first = self._delete(self.first, key)

    def _delete(self, x, key):
        if x is None:
            return None

        if key == x.key:
            self.N -= 1
            # return the next key-value pair to be chained
            return x.next

        # chains the post key-value pair to the previous of the one deleted
        x.next = self._delete(x.next, key)
        return x

# if __name__ == "__main__":
#     st = SequentialSearchST()
#     st.put(1, "Monkey")
#     st.put(42, "Pig")
#     st.put(10, "Rabbit")
#     print st.get(42)
#     st.put(1, "Elephant")
#     print st.get(1)
#     print st.size()
#     print st.delete(1)

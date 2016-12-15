class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    ## iterator protocol asks for definition of __iter__ and next ##
    def __iter__(self):
        return self._ReverseArrayIterator(self)

    ## encapsulated iterator in it's class so the main class won't have keep unnecessary information
    class _ReverseArrayIterator:
        def __init__(self, stack):
            self._arr = stack.items
            self._i = stack.size()

        def hasNext(self):
            return self._i > 0

        def next(self):
            if not self.hasNext():
                raise StopIteration
            # starts at the end & decreases to keep iteration in LIFO order
            self._i -= 1
            return self._arr[self._i]

## NOTE ON PYTHON: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice. ##

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
for i in stack:
    print i*2
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.pop())

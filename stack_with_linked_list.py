from linked_list import Node
from linked_list import LinkedList

class LinkedListStack(LinkedList):
    # will inherit init from LinkedList

    # will inherit isEmpty from LinkedList

    def push(self, item):
        new = Node(item)
        new.setNext(self.head)
        self.head = new

    def pop(self):
        item = self.head
        self.head = item.getNext()
        return item.getData()

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def __iter__(self):
        return self._ReverseLinkedListIterator(self)

    class _ReverseLinkedListIterator:
        def __init__(self, llist):
            self._current = llist.head

        def next(self):
            if self._current is None:
                raise StopIteration

            item = self._current.getData()
            # change for next iteration
            self._current = self._current.getNext()
            return item


stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
for i in stack:
    print i
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.pop())

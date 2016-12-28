from linked_list import Node
from linked_list import LinkedList

class LinkedListQueue(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new = Node(item)
        # if first node, it is both tail and head
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
        # otherwise, just add it to the end
            self.tail.setNext(new)
            self.tail = new

    def dequeue(self):
        old = self.head
        self.head = old.getNext()
        if self.isEmpty():
            last = None
        return old.getData()

    def __iter__(self):
        return self._LinkedListQueueIterator(self)

    class _LinkedListQueueIterator:
        def __init__(self, llist):
            # start at the head to keep FIFO order
            self._current = llist.head

        def next(self):
            if self._current is None:
                raise StopIteration

            item = self._current.getData()
            self._current = self._current.getNext()
            return item


queue = LinkedListQueue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
for i in queue:
    print "I been waiting for so long! -", i
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

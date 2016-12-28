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

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
for i in queue:
    print "I been waiting for so long! -", i
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

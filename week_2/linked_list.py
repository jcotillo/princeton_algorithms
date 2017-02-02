class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    # getters
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    #setters
    def setNext(self, nnext):
        self.next = nnext

    def setData(self, data):
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        new = Node(item)
        new.setNext(self.head)
        self.head = new

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        # need to keep track of last so if found, modify this one
        previous = None
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found and previous == None:
            # item was the head
            self.head = current.getNext()
        elif found:
            previous.setNext(current.getNext())

        return found

    def __iter__(self):
        return self._LinkedListIterator(self)

    class _LinkedListIterator:
        def __init__(self, llist):
            # start at the head to keep FIFO order
            self._current = llist.head

        def next(self):
            if self._current is None:
                raise StopIteration

            item = self._current.getData()
            self._current = self._current.getNext()
            return item

# list1 = LinkedList()
# list1.add(1)
# list1.add(2)
# list1.add(3)
# print list1.size()
# print list1.search(4)
# print list1.remove(4)
# print list1.remove(3)

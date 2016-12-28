from stack_with_array import Stack
# not very efficient.... o(n^2)
class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        size = self.stack1.size()
        if size == 0:
            self.stack1.push(item)
        else:
            while size > 0:
                self.stack2.push(self.stack1.pop())
                size -= 1
            self.stack2.push(item)
            size2 = self.stack2.size()
            while size2 > 0:
                self.stack1.push(self.stack2.pop())
                size2 -= 1

    def dequeue(self):
        return self.stack1.pop()

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print queue.dequeue()
print queue.dequeue()

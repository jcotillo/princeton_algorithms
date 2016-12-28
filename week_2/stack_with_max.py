class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        new_num = int(item)
        if len(self.max) == 0:
            self.max.append(new_num)
        elif new_num > self.max[len(self.max) - 1]:
            self.max.append(new_num)
        self.items.append(item)

    def pop(self):
        last = self.items.pop()
        if int(last) == self.max[len(self.max) - 1]:
            self.max.pop()
        return last

    def getMax(self):
        return self.max[len(self.max) - 1]

s = Stack()
s.push("1")
s.push("10")
s.push("100")
print s.getMax()
print s.pop()
print s.getMax()

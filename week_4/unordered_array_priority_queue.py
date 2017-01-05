class UnorderedMaxPQ:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0

    def insert(self, key):
        self.arr.append(key)

    def delMax(self):
        max = 0
        for i in range(1, len(self.arr)):
            if self.arr[i] > self.arr[max]:
                max = i
                self.arr[-1], self.arr[max] = self.arr[max], self.arr[-1]
        return self.arr.pop()

if __name__ == "__main__":
    pq = UnorderedMaxPQ()
    pq.insert(4)
    pq.insert(3)
    pq.insert(10)
    pq.insert(2)
    print pq.delMax()

class BinaryHeap:
    def __init__(self):
        # not using element at index 0 to be able do arithmetic to access heap structure by the indexes
        self.arr = ['x']
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def insert(self, key):
        self.arr.append(key)
        self.N += 1
        self._swim(self.N)

    def _swim(self, k):
        # parent node of k is at k/2
        while k > 1 and self.arr[k/2] < self.arr[k]:
            self.arr[k/2], self.arr[k] = self.arr[k], self.arr[k/2]
            k = k/2

    def delMax(self):
        self.arr[1], self.arr[self.N] = self.arr[self.N], self.arr[1]
        maxx = self.arr.pop()
        self.N -= 1
        self._sink(1)
        return maxx

    def _sink(self, k):
        while 2*k <= self.N:
            j = 2*k
            # children nodes of k are in arr[2*k] & arr[2*k + 1]
            if j < self.N and self.arr[j] < self.arr[j+1]:
                j += 1
            if self.arr[k] > self.arr[j]:
                break
            self.arr[k], self.arr[j] = self.arr[j], self.arr[k]
            k = j

if __name__ == "__main__":
    bh = BinaryHeap()
    bh.insert(1)
    bh.insert(10)
    bh.insert(21)
    bh.insert(19)
    bh.insert(11)
    bh.insert(4)
    bh.insert(40)
    print bh.delMax()
    print bh.delMax()

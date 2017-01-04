from random import shuffle
from quick_sort import _partition

#linear time selection algorithm that plays off quick sort
# k is the index of the desired selection in the SORTED array
#  k = 0; smallest item
#  k = len(arr) - 1, highest item
#  k len(arr) / 2, median item

def quick_selection(arr, k):
    shuffle(arr)
    low = 0
    high = len(arr) - 1

    while high > low:
        j = _partition(arr, low, high)
        if j < k:
            low = j + 1
        elif j > k:
            high = j - 1
        else:
            return arr[k]

    return arr[k]

if __name__ == "__main__":
    arr = [2, 1, 10, 56, 100, 12]
    print quick_selection(arr, len(arr) -1)

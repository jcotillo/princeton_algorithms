# Quick sort is an in-place sorting algorithm that
# runs 39% faster than merge sort, in the average case.
from random import shuffle

def quick_sort(arr):
    # shuffle is needed to guarantee performance
    shuffle(arr)
    _sort(arr, 0, len(arr) - 1)
#depth of recursion is going to be logarithmic
def _sort(arr, low, high):
    if high <= low:
        return
    j = _partition(arr, low, high)
    _sort(arr, low, j - 1)
    _sort(arr, j+1, high)
# quicksort is not stable b/c partition does long range exchanges
def _partition(arr, low, high):
    pivot = arr[low]
    i = low+1
    j = high
    done = False
    while not done:
        while i != high and arr[i] < pivot:
            i += 1

        while j != low and arr[j] > pivot:
            j -= 1

        if i >= j:
            done = True
        else:
            # stop before they cross, swap elements out of order & continue
            arr[i], arr[j] = arr[j], arr[i]

    #swap elements if the pointers crossed
    arr[low], arr[j] = arr[j], arr[low]
    return j

if __name__ == "__main__":
    arr = [9,8,1,21,5]
    quick_sort(arr)
    print arr

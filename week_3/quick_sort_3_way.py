from random import shuffle

def quick_sort(arr):
    shuffle(arr)
    _sort(arr, 0, len(arr) - 1)

def _sort(arr, low, high):
    if high <= low:
        return
    left = low
    right = high
    pivot = low
    value = arr[pivot]

    while pivot <= right:
        if arr[pivot] < value:
            arr[left], arr[pivot] = arr[pivot], arr[left]
            left += 1
            pivot += 1
        elif arr[pivot] > value:
            arr[right], arr[pivot] = arr[pivot], arr[right]
            right -= 1
        else:
            pivot += 1

    _sort(arr, low, left - 1)
    _sort(arr, right + 1, high)

if __name__ == "__main__":
    arr = [20, 21, 2, 43, 50, 20, 20, 3, 2, 40, 43]
    quick_sort(arr)
    print arr

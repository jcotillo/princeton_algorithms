def heap_sort(arr):
    n = len(arr)
    # set up binary heap
    for k in range(n/2, 0, -1):
        sink(arr, k, n)
    # order it now
    while n > 1:
        _exch(arr, 1, n)
        n -= 1
        sink(arr, 1, n)
    return arr

def sink(arr, k1, k2):
    while 2*k1 <= k2:
        j = 2*k1
        if j < k2 and _less(arr, j, j+1):
            # j needs to be BIGGEST child node for exchange
            j += 1
        # another check. break out before exchange if parent is greater...
        if not _less(arr, k1, j):
            break
        _exch(arr, k1, j)
        k1 = j

def _less(arr, i, j):
    # make it behave like it's 0 index
    return arr[i-1] < arr[j-1]

def _exch(arr, i, j):
    # make it behave like it's 0 index
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

if __name__ == '__main__':
    print heap_sort([9,8,31, 401, 23,1, 43,12, 32, 35, 39])

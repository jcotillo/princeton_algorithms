from merge_sort import _merge

def merge_sort_bu(arr):
    aux_ar = [None for i in range(len(arr))] #copy over

    sz = 1
    # First nested loop is "Size of the sub-array" executed only lg N times (lg N passes)
    while sz < len(arr):
        low = 0
        while low < (len(arr) - sz):
            mid = low + sz - 1
            high = min(low+sz+sz-1, len(arr)-1)
            _merge(arr, aux_ar, low, mid, high)
            low += sz+sz

        # double size everytime
        sz = sz+sz
    return arr

if __name__ == "__main__":
    print merge_sort_bu([6,5,3, 4, 1])

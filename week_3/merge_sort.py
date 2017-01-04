def merge_sort(arr):
    aux_ar = [None for i in range(len(arr))]
    #copy over
    for i in range(len(arr)):
        aux_ar[i] =  arr[i]

    _sort(arr, aux_ar, 0, len(aux_ar)-1)
    return arr

def _sort(arr, aux_ar, low, high):
    if high <= low:
        return
    mid = low + (high-low)/2
    _sort(arr, aux_ar, low, mid)
    _sort(arr, aux_ar, mid+1, high)
    _merge(arr, aux_ar, low, mid, high)

def _merge(arr, aux_ar, low, mid, high):
    i = low #left pointer
    j = mid+1 #right pointer
    aux_ar[low:high+1] = arr[low:high+1] # copy to aux_arr

    # k is pointer in main array
    for k in range(low, high+1):
        if i > mid:     # ran out on the left side
            arr[k] = aux_ar[j]
            j += 1
        elif j > high:  # ran out on the right side
            arr[k] = aux_ar[i]
            i += 1
        elif aux_ar[j] < aux_ar[i]:
            arr[k] = aux_ar[j]
            j += 1
        else:
            arr[k] = aux_ar[i]
            i += 1

# notes:
    # d(n) = n lg n
    # to prove: d(2n) = 2n lg (2n)

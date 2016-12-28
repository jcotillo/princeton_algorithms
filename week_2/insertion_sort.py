def insertion_sort(arr):
    for i in range(len(arr)):
        # inner loop goes through every element on the left and swaps if it is increasing order, otherwise passes it
        for j in range(i, 0, -1):
            # starts at i to work ONLY on the left hand size elements
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                pass
    return arr

if __name__ == "__main__":
    print insertion_sort([2,3,10,4])

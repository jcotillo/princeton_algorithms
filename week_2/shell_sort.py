# using 3x+1 increments
def shell_sort(arr, h=1):
    n = len(arr)
    while h < n/3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, len(arr)):
            for j in range(len(arr)-1, 0, -h):
                print j, i
                if arr[j] < arr[j-h]:
                    arr[j], arr[j-h] = arr[j-h], arr[j]
        h = h/3
    return arr

if __name__ == "__main__":
    print shell_sort([10,12,15,3,2,5,3,19, 22, 25])

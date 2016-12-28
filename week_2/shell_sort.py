# using 3x+1 increments
### to finish!!!
def shell_sort(arr, h=1):
    while h < len(arr)/3:
        h = 3*h + 1
    print h
    while h >= 1:
        for i in range(h, len(arr)):
            for j in range(len(arr) -1, i, -h):
                print i, j
                if j >= h:
                    pass
                if arr[j] < arr[j-h]:
                    arr[j], arr[j-h] = arr[j-h], arr[j]
            print "Arr now:", arr
        h = h/3
    return arr

if __name__ == "__main__":
    print shell_sort([10,12,15,3,2,5,3,19, 22, 25])

# can be applicable in such question: Intersection of two sets. Given two arrays 𝚊[] and 𝚋[], each containing n distinct 2D points in the plane, design a subquadratic algorithm to count the number of points that are contained both in array 𝚊[] and array 𝚋[].

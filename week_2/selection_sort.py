def selection_sort(items):
    for i in range(len(items)):
        for j in range(i,len(items)):
            # by starting at i, works ONLY on the right hand side elements
            if items[j] < items[i]:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp

    return items

if __name__ == '__main__':
    print selection_sort([4,5,2,1,3])

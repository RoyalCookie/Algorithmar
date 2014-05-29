def insertionSort(array):
    a = 0
    for x in range(0, len(array)):
        insertionSortHelper(array, x, a)

def insertionSortHelper(array, x, a):
    if(x-1 >= 0):
        if(array[x] < array[x-1]):
            a = array[x-1]
            array[x-1] = array[x]
            array[x] = a
            a = 0
            insertionSortHelper(array, x-1, a)


listi = [12,53,21,24,65,45,87,26,42,48]

insertionSort(listi)



for x in range(0, len(listi)):
    print(listi[x])


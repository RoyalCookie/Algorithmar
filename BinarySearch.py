import  math

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


def splitArray(array):
    array1 = []
    array2 = []
    counter = 0
    for variable in array:
        if(counter  <= (math.ceil(len(array)/2)-1)):
            array1.append(array[counter])
            print("added to array 1")
        else:
            array2.append(array[counter])
            print("added to array 2")
        counter += 1
    t = (array1,array2)
    return t
def printDoubleArray(t):
    for array in t:
        for variable in array:
            print(variable)
        print("\n ----------- \n")


def binarySearch(array, x):
    start = 0
    end = len(array)-1
    while(start <= end):
        mid = int(math.ceil(start+end)/2)
        if(array[mid] == x):
            return mid
        elif(array[mid] > x):
            end = mid - 1
        elif(array[mid] < x):
            end = mid + 1
    return -1





listi = [12,53,21,24,65,45,87,26,42,48]
insertionSort(listi)
print(binarySearch(listi, 12))








#print(binarySearch(listi, 24))

printDoubleArray(splitArray(listi))

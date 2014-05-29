import random

def selectPivot(array):
    length = len(array)
    pArray = []
    for x in range(0,3):
        tempSelector = random.randint(0, length-1)
        pArray.append((array[tempSelector],tempSelector))
    pArray.sort()
    #print(pArray[1])
    return pArray[1][1]



def quickSort(array):
    print("called Once" + str(array))

    if len(array) <= 1:
        return array
    mP = selectPivot(array)

    lowArr = []
    hiArr = []
    for x in range(0, len(array)):
        if array[x] < array[mP] and x != mP:
            lowArr.append(array[x])
        if array[x] > array[mP] and x != mP:
            hiArr.append(array[x])

    reArr = []
    hiArr = quickSort(hiArr)
    lowArr = quickSort(lowArr)
    for x in lowArr:
        reArr.append(x)
    reArr.append(array[mP])
    for x in hiArr:
        reArr.append(x)
    return reArr

tala = []
for x in range(0,15):
    tala.append(random.randint(1,120))

print(quickSort(tala))
print(tala)
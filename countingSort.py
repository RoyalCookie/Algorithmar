import random


def countingSort(array):
    countArray = []
    finalArray = []
    tempTala = 0

    # Find Maximum Number
    for tala in array:
        if tala > tempTala:
            tempTala = tala

    # Create Empty Array Large As Biggest Number
    for x in range(0,tempTala+1):
        countArray.append(0)

    # Count into array
    for x in array:
        countArray[x] = countArray[x] + 1


    print(countArray)

    # Move From Count Array Into Return Array
    for x in range(0, len(countArray)):
        for z in range(0, countArray[x]):
            finalArray.append(x)

    return finalArray




tala = []
for x in range(0,5):
    tala.append(random.randint(1,15))
print(tala)
print(countingSort(tala))
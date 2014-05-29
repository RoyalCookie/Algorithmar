import random

def unifyNumbers(array):
    #Largest Length of Numbers
    lN = 0
    # Find the Largest Length of Number
    for x in array:
        if len(x) > lN:
            lN = len(x)
    #Add The Zeros for each diffrence
    for x in range(0,len(array)):
        dif = lN - len(array[x])
        for z in range(0,dif):
            array[x] = str("0" + array[x])

    return lN


def radixSort(array):
    length = unifyNumbers(array)
    bucketArr = []
    for x in range(0,10):
        bucketArr.append([])
    #########################################
    # Fill bucket array - Looks to be working
    for i in range(length-1, -1, -1):
        for a in range(0,len(array)):
            for b in range(0,10):
                if array[a][i] == str(b):
                    bucketArr[b].append(str(array[a]))

        #########################################
        # Clear Normal Array
        del array[:]

        #########################################
        #Append Bucket to normal Array
        for a in bucketArr:
            for b in a:
                array.append(b)
        print(array)

        #########################################
        #Clear Bucket
        for x in range(0, len(bucketArr)):
            del bucketArr[x][:]




tala = []
for x in range(0,5):
    tala.append(str(random.randint(1,120)))
    tala.append(str(random.randint(1,5000)))



print(tala)
radixSort(tala)
print(tala)
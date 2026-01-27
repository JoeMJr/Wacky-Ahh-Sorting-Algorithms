import random
import math

def isSorted(list):
    return all(list[i] <= list[i+1] for i in range(len(list) - 1)) # Oneliner from stackoverflow

def bogoSort(list):
    while not isSorted(list):
        random.shuffle(list)
    return list

def stalinSort(list):
    # This is really stupid and I am really stupid
    count = 0
    last_num = 0
    #print((range(len(list)-1)))
    newlist = []
    for i in (range(len(list)-1)):
        if ((last_num > list[count]) & (count > 0)):
            print("No item added, ", list[count])
        else:
            newlist.append(list[count])
            last_num = list[count]
        count = count + 1
    newlist.append(list[count])
    return newlist

# might add Stooge sort
# https://en.wikipedia.org/wiki/Stooge_sort

def arraySwap(list, pos1, pos2):
    # Swapping two var without a temp var
    #print("BEFORE, A: ", list[pos1], " , B: ", list[pos2])
    list[pos1] = list[pos1] + list[pos2]
    #print("A: ", list[pos1], " , B: ", list[pos2])
    list[pos2] = list[pos1] - list[pos2] # MY DUMBASS ACCIDENTLY HAD THE SECOND ONE AS pos1 instead of pos2
    #print("A: ", list[pos1], " , B: ", list[pos2])
    list[pos1] = list[pos1] - list[pos2]
    #print("AFTER, A: ", list[pos1], " , B: ", list[pos2])
    


def stoogeSort(list, i, j):
    #print("List[0]: ", type(list[0]))
    if list[i] > list[j]:
        arraySwap(list, i, j)
    if (j - i + 1) > 2:
        t = math.floor((j-i+1)/3)
        stoogeSort(list, i, j-t)
        stoogeSort(list, i+t, j)
        stoogeSort(list, i, j-t)
    return list

# https://en.wikipedia.org/wiki/Slowsort Multiply and surrender
# SlowSort
def slowSort(list, startIndex, endIndex):
    # Inplace sort that doesn't return a list
    if startIndex >= endIndex:
        return
    
    middleIndex = math.floor((startIndex + endIndex)/2)

    slowSort(list, startIndex, middleIndex)
    slowSort(list, middleIndex + 1, endIndex)

    if list[endIndex] < list[middleIndex]:
        arraySwap(list, endIndex, middleIndex)
    
    slowSort(list, startIndex, endIndex - 1)



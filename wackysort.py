import random
import math
#import pytest

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
    if list[pos1] == list[pos2]:
        return

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

# Gnome Sort (Stupid Sort)
def gnomeSort(list):
    pos = 1
    while pos < len(list):
        if pos == 0 or list[pos] >= list[pos-1]:
            pos = pos + 1
        else:
            arraySwap(list, pos, (pos-1))
            pos = pos -1

# Not Dogwater Sorting Algorithms

# Quick Sort
def quickSort(list, low, high):
    # Base Case
    if low >= high or low < 0:
        return
    partIndex = partition(list, low, high)

    # Recursion bit
    quickSort(list, low, partIndex - 1)
    quickSort(list, partIndex + 1, high)
    
def partition(list, low, high):
    pivot = list[high]

    tempIndex = low

    for j in range(low, high):
        if list[j] <= pivot:
            # print("J: ", j, ", tempIdx: ", tempIndex) # TEMP PRINT FOR TESTING
            arraySwap(list, tempIndex, j)
            tempIndex = tempIndex + 1

    arraySwap(list, tempIndex, high)

    return tempIndex

# Radix Sort
def radixSort(list):
    currentMax = max(list)

    currentDigits = 1
    while currentMax / currentDigits >= 1:
        countSort(list, currentDigits)
        currentDigits *= 10

def countSort(list, digits):
    
    listLen = len(list)

    output = [0] * (listLen)

    count = [0] * 10

    for i in range(0, listLen):
        index = list[i] // digits
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = listLen - 1
    while i >= 0:
        index = list[i] // digits
        output[count[index % 10] - 1] = list[i]
        count[index % 10] -= 1
        i -= 1
    
    j = 0
    for j in range(0, listLen):
        list[j] = output[j]

# Merge Sort
def merge(list, start, middle, end):
    start2 = middle + 1
    
    if list[middle] <= middle and start2 <= end:
        return 
    
    while start <= middle and start2 <= end:
        if list[start] <= list[start2]: 
            start = start + 1
        else:
            tempValue = list[start2]
            currentIndex = start2

            while currentIndex != start:
                list[currentIndex] = list[currentIndex - 1]
                currentIndex = currentIndex - 1
            
            list[start] = tempValue

            start += 1
            middle += 1
            end += 1




def mergeSort(list, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        middle = leftIndex + (rightIndex - leftIndex) // 2

        mergeSort(list, leftIndex, middle)
        mergeSort(list, (middle + 1), rightIndex)

        merge(list, leftIndex, middle, rightIndex)

# Final Good Sort
def countingSort(list):
    count = [0] * (1)
    output = [] * len(list)


# TESTING STUFF
# arr = [7, 24, 3, 43, 55]
# print("ARR: ", arr)
#mergeSort(arr, 0, (len(arr) - 1))
# gnomeSort(arr)
# print("ARR: ", arr)
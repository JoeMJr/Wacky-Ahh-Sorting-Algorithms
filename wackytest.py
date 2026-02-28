import wackysort
import random
from datetime import datetime
# import pytest # I need to add benchmarking for some of these functions
# Use below guide
# https://codspeed.io/docs/guides/how-to-benchmark-python-code

# Old Test Arrays
#test1 = [1, 2, 3, 4, 5]
#test2 = [7, 24, 3, 43, 55]
#test3 = [3, 2, 1, 4, 5]
#test4 = [1, 2, 3, 4, 5]
#test5 = [1, 2, 3, 4, 5]

#test_cases = [test1, test2, test3, test4, test5]

# I need to flesh out these test sets

def testCaseGenerator(listLen, testRangeMax = 9):
    testList = []
    for i in range(listLen):
        testList.append(random.randint(1, testRangeMax))
        # testList[i] = random.randint(1, testRangeMax) # I WAS STUPID

    return testList


# Simple tests
# print("Bogo Sort test 2:", wackysort.bogoSort(test2))
# print("Stooges sort for test 2: ", wackysort.stoogeSort(test2, 0, (len(test2)-1)))
#print("BEFORE Slow sort for test 2: ", test2)
#wackysort.slowSort(test2, 0, (len(test2)-1)) # Inplace sort that doesn't return a list
#print("Slow sort for test 2: ", test2)
#print("Quick test outside of thing. Arr:", test2)
#wackysort.quickSort(test2, 0, (len(test2)-1))
#print("AFTER, Arr: ", test2)

# Comprehensive tests with random lists and Benchmarking
# Bad
def stoogeTest(arr):
    wackysort.stoogeSort(arr, 0 , (len(arr)-1) )

def slowTest(arr):
    wackysort.slowSort(arr, 0, (len(arr)-1))

def stalinSort(arr):
    wackysort.stalinSort(arr)

def gnomeSort(arr):
    wackysort.gnomeSort(arr)

# I am not adding bogo sort since it is the stupidest and literally worst case infinite
# nvm LOL
def bogoTest(arr):
    wackysort.bogoSort(arr)

# Good
def quickTest(arr):
    wackysort.quickSort(arr, 0, (len(arr)-1))

def radixTest(arr):
    wackysort.radixSort(arr)

def mergeTest(arr):
    wackysort.mergeSort(arr, 0, (len(arr)-1))

def countTest(arr):
    wackysort.countingSort(arr)

# Main Function
def sortBechmark(log_id, sortCode, sortAmount, sortMax):
    testArr = testCaseGenerator(sortAmount, sortMax)
    
    log_file = "sortLog" + log_id + ".txt"
    outfile = open(log_file, 'w', encoding="utf8")
    now = datetime.now()
    print("Start Time =", now)
    outfile.write("Sorting Log " + log_id + "\n")
    outfile.write("Start Time =" + str(now) + "\n")
    # 
    if sortCode == 0:
        print("Stooge Test")
        outfile.write("Stooge Test\n")
        stoogeTest(testArr)
        if wackysort.isSorted(testArr):
            print("Stooge Test Success")
            outfile.write("Stooge Test Success\n")
        else:
            print("Stooge Test Failure")
            outfile.write("Stooge Test Failure\n")

    elif sortCode == 1:
        print("Slow Test")
        outfile.write("Slow Test\n")
        slowTest(testArr)
        if wackysort.isSorted(testArr):
            print("Slow Test Success")
            outfile.write("Slow Test Success\n")
        else:
            print("Slow Test Failure")
            outfile.write("Slow Test Failure\n")

    elif sortCode == 2:
        print("Quick Test")
        outfile.write("Quick Test\n")
        quickTest(testArr)
        if wackysort.isSorted(testArr):
            print("Quick Test Success")
            outfile.write("Quick Test Success\n")
        else:
            print("Quick Test Failure")
            outfile.write("Quick Test Failure\n")

    elif sortCode == 3:
        print("Radix Test")
        outfile.write("Radix Test\n")
        radixTest(testArr)
        if wackysort.isSorted(testArr):
            print("Radix Test Success")
            outfile.write("Radix Test Success\n")
        else:
            print("Radix Test Failure")
            outfile.write("Radix Test Failure\n")

    elif sortCode == 4:
        print("Stalin Test")
        outfile.write("Stalin Test\n")
        tempArr = stalinSort(testArr)
        if wackysort.isSorted(tempArr):
            print("Stalin Test Success")
            outfile.write("Stalin Test Success\n")
        else:
            print("Stalin Test Failure")
            outfile.write("Stalin Test Failure\n")

    elif sortCode == 5:
        print("Gnome Test")
        outfile.write("Gnome Test\n")
        gnomeSort(testArr)
        if wackysort.isSorted(testArr):
            print("Gnome Test Success")
            outfile.write("Gnome Test Success\n")
        else:
            print("Gnome Test Failure")
            outfile.write("Gnome Test Failure\n")

    elif sortCode == 6:
        print("Merge Test")
        outfile.write("Merge Test\n")
        mergeTest(testArr)
        if wackysort.isSorted(testArr):
            print("Merge Test Success")
            outfile.write("Merge Test Success\n")
        else:
            print("Merge Test Failure")
            outfile.write("Merge Test Failure\n")
    
    elif sortCode == 7:
        print("Count Test")
        outfile.write("Count Test\n")
        countTest(testArr)
        if wackysort.isSorted(testArr):
            print("Count Test Success")
            outfile.write("Count Test Success\n")
        else:
            print("Count Test Failure")
            outfile.write("Count Test Failure\n")
        
    else:
        print("Invalid Sorting Test")
        outfile.write("INVALID TEST\n")
    # end 
    later = datetime.now()
    print("End Time =", later)
    outfile.write("End Time =" + str(later) + "\n")
    timmDiff = later - now

    print("Time Elapsed: " + str(timmDiff))
    outfile.write("Time Elapsed: " + str(timmDiff) + "\n")

    outfile.close()
    print("Ending Benchmark")


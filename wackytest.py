import wackysort

test1 = [1, 2, 3, 4, 5]
test2 = [7, 24, 3, 43, 55]
test3 = [3, 2, 1, 4, 5]
test4 = [1, 2, 3, 4, 5]
test5 = [1, 2, 3, 4, 5]

test_cases = [test1, test2, test3, test4, test5]

# I need to flesh out these test sets

# Simple tests
# print("Bogo Sort test 2:", wackysort.bogoSort(test2))
# print("Stooges sort for test 2: ", wackysort.stoogeSort(test2, 0, (len(test2)-1)))
print("BEFORE Slow sort for test 2: ", test2)
wackysort.slowSort(test2, 0, (len(test2)-1)) # Inplace sort that doesn't return a list
print("Slow sort for test 2: ", test2)

# Comprehensive tests with random lists and Benchmarking



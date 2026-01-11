import random

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
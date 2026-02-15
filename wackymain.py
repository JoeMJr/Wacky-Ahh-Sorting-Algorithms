import wackytest
import os

index_file = "index.txt"
choice = 1
option = 1
id = 0

while choice is not 0:
    print("Wacky Tests Main")
    print("1. Stooge Test")
    print("2. Slow Test")
    print("3. Quick Test")
    print("4. Radix Test")
    choice = input("What do you want to do?\n")
    #print(type(choice))
    choice = int(choice)
    if choice == 0:
        print("ending main")
    elif choice >= 1 and choice <= 4:
        option = input("What magnitude do you want to?\n")
        option = int(option)
        if option <= 1 or option >= 10:
            print("Invalid magnitude")
        else:
            my_file = open(index_file, "r")
            id = my_file.read()
            my_file.close()
            wackytest.sortBechmark(id, (choice - 1), (10**option), 100)
            outfile = open(index_file, "w")
            print("ID: ", id, ", Type: ", type(id))
            outfile.write(str(int(id)+1))
            outfile.close()
    else:
        print("Please use one of the actual options")



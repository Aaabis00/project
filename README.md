# Menu Driven Of all Data structure built in functions

// Main file[MainMenuDrivenfile.py](https://github.com/user-attachments/files/26333670/MainMenuDrivenfile.py)
from Menudrivenofallbuiltinfunctionofdatastructure2 import listbuiltin, dictbuiltin, tuplebuiltin, setbuiltin, stringbuiltin

print("Menu driven of all Data structure built in function")

while True:
    print("\nMenu Driven")
    print("1. List")
    print("2. Dictionary")
    print("3. Tuple")
    print("4. Sets")
    print("5. String")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice not in[1, 2, 3, 4, 5, 6]:
            print("Enter the number btw 1 to 6")
            continue
    except ValueError:
        print("Enter only integer numbers")
        continue

    if(choice == 1):
        print("Calling list function..")
        listbuiltin()
        input("Press Enter to Continue..")

    elif(choice == 2):
        print("Calling dict function")
        dictbuiltin()
        input("Press Enter to Continue..")

    elif(choice == 3):
        print("Calling tuple function....")
        tuplebuiltin()
        input("Press Enter to Continue..")

    elif(choice == 4):
        print("Calling Set function")
        setbuiltin()
        input("Press Enter to Continue..")

    elif(choice == 5):
        print("Calling String Function")
        stringbuiltin()
        input("Press Enter to Continue..")

    elif(choice == 6):
        print("Exiting...")
        break

    else:
        print("Invalid number or choice")



// function file 


[Menudrivenofallbuiltinfunctionofdatastructure2.py](https://github.com/user-attachments/files/26333676/Menudrivenofallbuiltinfunctionofdatastructure2.py)
# list bulit in functions
def listbuiltin():
    while True:
        print("Select a number to which built in function you want to see")
        print("1 to see append() function")
        print("2 to see copy() function")
        print("3 to see clear() function")
        print("4 to see count() function")
        print("5 to see extend() function")
        print("6 to see index() function")
        print("7 to see insert() function")
        print("8 to see pop() function")
        print("9 to see remove() function")
        print("10 to see reverse() function")
        print("11 to see sort() function")
        print("12 to exit")

        try:
            a = int(input("Enter your choice: "))
            if a not in[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                print("Enter the number btw 1 to 12 only")
                continue
        except ValueError:
            print("Enter integer only")
            continue


        my_list = [10, 20, 30, 40, 30]


        if(a == 1):
            print("Append() function is used to add an element to the end of the list")
            my_list.append(4)
            print(my_list)

        elif(a == 2):
            print("copy() function returns a shallow copy of the list")
            b = my_list.copy()
            print(b)

        elif(a == 3):
            print("clear() function is used to clear the list")
            my_list.clear()
            print(my_list)

        elif(a == 4):
            print("count() function will count the occurance of an specific element how many times it is occured ")
            print(my_list.count(30))

        elif(a == 5):
            print("extend() function is used to extend the list from other list")
            my_list.extend([7, 8])
            print(my_list)

        elif(a == 6):
            print("index() function is to find the index of a specific element")
            print(my_list.index(40))

        elif(a == 7):
            print("insert() function is used to insert an element at a specific position in the list")
            my_list.insert(1, 5698)
            print(my_list)

        elif(a == 8):
            print("pop() function is used to pop the last element of the list")
            my_list.pop()
            print(my_list)

        elif(a == 9):
            print("remove() function is used to remove the first occurrence of a specified element from the list")
            my_list.remove(30)
            print(my_list)

        elif(a == 10):
            print("reverse() function is used to reverse the order of the elements in the list")
            my_list.reverse()
            print(my_list)

        elif(a == 11):
            print("sort() function is used to sort the list in ascending order")
            print("before sort(): ", my_list)
            my_list.sort()
            print("after sort(): ", my_list)

        elif(a == 12):
            print("Exiting...")
            break

        else:
            print("Select the correct input the entered number is wrong input")

# dictionary built in
def dictbuiltin():
    while True:
        print("Select a number to which function you want to see")
        print("1 to see clear() function")
        print("2 to see get() function")
        print("3 to see items() function")
        print("4 to see keys() function")
        print("5 to see update() function")
        print("6 to see values() function")
        print("7 to see pop() function")
        print("8 to see popitem() function")
        print("9 to exit")

        my_dict = {'Name' : 'Abhi', 'Age' : 23, 'Country':'India'}


        try:
            a = int(input("Enter your choice: "))
            if a not in[1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Enter the number btw 1 to 9")
                continue
        except ValueError:
            print("Enter integer only")
            continue

        if(a == 1):
            print("clear() function is used to clear the dictionary")
            my_dict.clear()
            print(my_dict)

        elif(a == 2):
            print("get() function help to obtain the value linked to a particular key in the dictionary")
            print(my_dict.get('Name'))
            print(my_dict.get('Country'))

        elif(a == 3):
            print("items() function is used that retrieves a view object containing a list of tuples")
            print(list(my_dict.items())[1][0])
            print(list(my_dict.items())[1][1])

        elif(a == 4):
            print("keys() function is used return a view object with dictionary keys")
            print(my_dict.keys())

        elif(a == 5):
            print("update() function is used to uspade the the elements in the dictionary from other dictionary")
            dict2 = {'Name' : 'xyz', 'Age':56}
            my_dict.update(dict2)
            print(my_dict)

        elif(a == 6):
            print("values() function is used to return a view object containing all dictionary values")
            print(my_dict.values())

        elif(a == 7):
            print("pop() function is used to pop the value using its key")
            my_dict.pop('Age')
            print(my_dict)

        elif(a == 8):
            print("popitem() function is used to pop the last inserted key value")
            my_dict.popitem()
            print(my_dict)
            my_dict.popitem()
            print(my_dict)

        elif(a == 9):
            print("Exiting...")
            break

        else:
            print("Enter the correct number")

# tuple built in
def tuplebuiltin():
    while True:
        print("Select which build in function you want to see in tuple")
        print("1 to see len() function")
        print("2 to see max() function")
        print("3 to see min() function")
        print("4 to see sum() function")
        print("5 to see sorted() function")
        print("6 to exit")

        my_tuple = (10, 30, 20)
        try:
            a = int(input("Enter your choice: "))
            if a not in[1, 2, 3, 4, 5, 6]:
                print("Enter the number btw 1 to 6")
                continue
        except ValueError:
            print("Enter integer only")
            continue

        if(a == 1):
            print("len() function is used to find the number of elements in the tuple")
            print(len(my_tuple))

        elif(a == 2):
            print("max() function is used to find the maximum element in the tuple")
            print(max(my_tuple))

        elif(a == 3):
            print("min() function is used to find the minimum element in the list")
            print(min(my_tuple))

        elif(a == 4):
            print("sum() function is used to find the sum of all the elements present in the tuple")
            print(sum(my_tuple))
    
        elif(a == 5):
            print("sorted() function is used to sort the elements in the tuple in ascending order")
            print(sorted(my_tuple))

        elif(a == 6):
            print("Exiting...")
            break

        else:
            print("Choose the correct number")
    
# set built in
def setbuiltin():
    while True:
        print("Select a number to see which function you want to perform")
        print("1 to see add() function")
        print("2 to see discard() function")
        print("3 to see remove() function")
        print("4 to see pop() function")
        print("5 to see clear() function")
        print("6 to exit")

        my_set = {1, 2, 3, 4, 5}
        try:
            a = int(input("Enter your choice: "))
            if a not in[1, 2, 3, 4, 5, 6]:
                print("Enter the number btw 1 to 6")
                continue
        except ValueError:
            print("Enter integer only")
            continue

        if(a == 1):
            print("add() function is used to add a element in the set")
            my_set.add(50)
            print(my_set)

        elif(a == 2):
            print("discard() function is used to discard an element from the set")
            my_set.discard(4)
            print(my_set)

        elif(a == 3):
            print("remove() function is used to remove a element from the set")
            my_set.remove(5)
            print(my_set)

        elif(a == 4):
            print("pop() function is used to pop an element from the set")
            my_set.pop()
            print(my_set)

        elif(a == 5):
            print("clear() functon is used to clear the set")
            my_set.clear()
            print(my_set)

        elif(a == 6):
            print("Exiting...")
            break

        else:
            print("Enter the correct number") 

# string built in
def stringbuiltin():
    while True:
        print("Select a number to see what function you want to see")
        print("1 to see upper() function")
        print("2 to see lower() function")
        print("3 to see title() function")
        print("4 to see swapcase() function")
        print("5 to capitalize() function")
        print("6 to exit")

        my_str = 'my nAme iS AbhiShek'
        try:
            a = int(input("Enter your choice: "))
            if a not in[1, 2, 3, 4, 5, 6]:
                print("Enter the number btw 1 to 6")
                continue
        except ValueError:
            print("Enter integer only")
            continue

        if(a == 1):
            print("upper() function is used to convert the string into uppercase")
            print("Before: ", my_str)
            print(my_str.upper())

        elif(a == 2):
            print("lower() function is used to convert the string into lowercase")
            print("Before: ", my_str)
            print(my_str.lower())

        elif(a == 3):
            print("title() function is used to convert the first character to upparcase")
            print("Before: ", my_str)
            print(my_str.title())

        elif(a == 4):
            print("swapcase() function is used to convert all string in lower to upper and viceversa ")
            print("Before: ", my_str)
            print(my_str.swapcase())

        elif(a == 5):
            print("capitalize() function is used to convert the first character into uppercase")
            print("Before: ", my_str)
            print(my_str.capitalize())

        elif(a == 6):
            print("Exiting...")
            break

        else:
            print("Enter the correct number")

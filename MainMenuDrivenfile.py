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

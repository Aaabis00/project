from NumberAnalayzerSystem2 import prime, armstrong, perfect, palindrome, revese, sumofdigits

print("Number Analyzer")

while True:
    print("\nMenu")
    print("1. Prime number")
    print("2. Armstrong number")
    print("3. Perfect number")
    print("4. Plindrome number")
    print("5. Reverse of a number")
    print("6. Sum of digits")
    print("7. Exit")

    # User input for choice
    try:
        choice = int(input("Enter your choice: "))
        if choice not in[1, 2, 3, 4, 5, 6, 7]:
            print("The number must be in the range of 1 to 7")
            continue
    except:
        print("Invalid choice! Enter Number only and number from 1 to 7")
        continue

    if choice == 7:
        print("Exiting..")
        break

    # user number for input
    try:
        num = int(input("Enter a number: "))
    except:
        print("Invalid number! Enter integer number only")
        continue

    if(choice == 1):
        prime(num)
    elif(choice == 2):
        armstrong(num)
    elif(choice == 3):
        perfect(num)
    elif(choice == 4):
        palindrome(num)
    elif(choice == 5):
        revese(num)
    elif(choice == 6):
        sumofdigits(num)
    else:
        print("Invalid choice")

    
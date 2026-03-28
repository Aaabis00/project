# fuction to check prime
def prime(num):
    if(num <= 1):
        print("Not a prime number")
    
    flag = 0
    for i in range(2, num):
        if(num % i == 0):
            flag = 1
            break
    if(flag == 0):
        print("The number is prime")
    else:
        print("Not a prime number")

# Armstrong number
def armstrong(num2):
    temp = num2
    total = 0 

    while(temp > 0):
        digit = temp % 10
        total = total + (digit * digit * digit)
        temp = temp // 10

    if(total == num2):
        print("The number is Armstrong number")
    else:
        print("The entered number is not an Armstrong number")

# Perfect number
def perfect(num3):
    total = 0
    for i in range (1, num3):
        if(num3 % i == 0):
            total = total + i
    
    if(total == num3):
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number")

# palindrome number
def palindrome(num):
    rev = 0
    temp = num
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if(temp == rev):
        print("The number is a palindrome number")
    else:
        print("The number is not a palindrome number")

# revese of number
def revese(num):
    rev = 0
    temp = num
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print("Before revese: ",temp)
    print("After revese: ", rev)

# sum of digits
def sumofdigits(num):
    sum = 0
    while(num > 0):
        digit = num % 10
        sum = sum + digit
        num = num // 10
    
    print("The sum of the entered number are: ", sum)
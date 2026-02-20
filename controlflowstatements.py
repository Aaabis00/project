# control flow statements 
# if statement
# if condition
# block of code
# examples of if else
setflag = True
if setflag:
    print("Hello everyone!!")
    print("solve the assignment")
print("executed true")

setflag = False
if setflag:
    print("good afternoon everyone")
    print("solve the assignment")
print("Executed false")

# 2nd example
no = 3
if no < 5:
    print("Number is less than 5")

# if else condition syntax
# if condition:
#   block of if
# else:
#   block of else

no=int(input("Enter a number to see if the number is even or odd: "))
if no % 2 == 0:
    print("number is even")
else:
    print("Number is odd")

# elif code syntax
# if condition:
#   block of if
# elif condition 2
#   block of elif
# elif condition 3
#   block of elif
# else
#   block of else

no =int(input("Enter a number to see if it is positive or negative or 0: "))
if no >0:
    print("The number is positive")
elif no<0:
    print("The number is negative")
else:
    print("The number is 0")

# questions to solve 
# 1st check wheather a person is eligible for voting accept the age from the user
# 2nd display "attendence is manditory for lectures" if the entered number is divisible by 5 otherwise diplay "bye, see you"
# 3rd display last digit of the number 
# 4th check wheather the last of a number entered by the user is divisible by 5
# 5th check wheather the year entered by the user is a leap year or not 

# 1st
no = int(input("Enter your age to see if ou are eligible for voting or not: "))
if no >= 18:
    print("you are eligible for voting")
else:
    print("You are not eligible for voting")

# 2nd
no = int(input("Enter a number: "))
if no % 5 == 0:
    print("Attendence is manditory for lectures")
else:
    print("bye, see you soon")

# 3rd
no = int(input("Enter a number to see its last digit: "))
a = no % 10
print("last digit is: ", a)

# 4th
no = int(input("Enter a number to see the last digit and if the last digit is divisible by 5 or not: "))
a = no % 10
print("last digit: ", a)

if a % 5 == 0:
    print("yes the last digit is divisible by 5")
else:
    print("no the last digit is not divisible by 5")

# 5th 
no = int(input("Enter a year to see if the yeear is a leap year or not: "))
if (no % 400 == 0) or (no % 4 == 0 and no % 100 != 0):
    print("The year entered is a leap year")
else:
    print("The year entered is not a leap year")
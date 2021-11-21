# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# printed a greetings
print ("\nWelcome! This program can arrange four (4) numbers from highest to lowest.")

# ask inputs from the user
firstNum = float(input("\nEnter your first number: "))
secondNum = float(input("Enter your second number: "))
thirdNum = float(input("Enter your third number: "))
fourthNum = float(input("Enter your fourth number: "))

# if elif else conditions of 24 possible results

# six (6) possible results if the first number is the highest number
if firstNum > secondNum > thirdNum > fourthNum:
    print (f"\nDescending order: {firstNum}, {secondNum}, {thirdNum}, {fourthNum} \n")
elif firstNum > thirdNum > fourthNum > secondNum:
    print (f"\nDescending order: {firstNum}, {thirdNum}, {fourthNum}, {secondNum} \n")
elif firstNum > fourthNum > secondNum > thirdNum:
    print (f"\nDescending order: {firstNum}, {fourthNum}, {secondNum}, {thirdNum} \n")
elif firstNum > secondNum > fourthNum > thirdNum:
    print (f"\nDescending order: {firstNum}, {secondNum}, {fourthNum}, {thirdNum} \n")
elif firstNum > thirdNum > secondNum > fourthNum:
    print (f"\nDescending order: {firstNum}, {thirdNum}, {secondNum}, {fourthNum} \n")
elif firstNum > fourthNum > thirdNum > secondNum:
    print (f"\nDescending order: {firstNum}, {fourthNum}, {thirdNum}, {secondNum} \n")

# six (6) possible results if the second number is the highest number
elif secondNum > firstNum > thirdNum > fourthNum:
    print (f"\nDescending order: {secondNum}, {firstNum}, {thirdNum}, {fourthNum} \n")
elif secondNum > thirdNum > fourthNum > firstNum:
    print (f"\nDescending order: {secondNum}, {thirdNum}, {fourthNum}, {firstNum} \n")
elif secondNum > fourthNum > firstNum > thirdNum:
    print (f"\nDescending order: {secondNum}, {fourthNum}, {firstNum}, {thirdNum} \n")
elif secondNum > thirdNum > firstNum > fourthNum:
    print (f"\nDescending order: {secondNum}, {thirdNum}, {firstNum}, {fourthNum} \n")
elif secondNum > firstNum > fourthNum > thirdNum:
    print (f"\nDescending order: {secondNum}, {firstNum}, {fourthNum}, {thirdNum} \n")
elif secondNum > fourthNum > thirdNum > firstNum:
    print (f"\nDescending order: {secondNum}, {fourthNum}, {thirdNum}, {firstNum} \n")

# six (6) possible results if the third number is the highest number
elif thirdNum > firstNum > secondNum > fourthNum:
    print (f"\nDescending order: {thirdNum}, {firstNum}, {secondNum}, {fourthNum} \n")
elif thirdNum > firstNum > fourthNum > secondNum:
    print (f"\nDescending order: {thirdNum}, {firstNum}, {fourthNum}, {secondNum} \n")
elif thirdNum > secondNum > firstNum > fourthNum:
    print (f"\nDescending order: {thirdNum}, {secondNum}, {firstNum}, {fourthNum} \n")
elif thirdNum > secondNum > fourthNum > firstNum:
    print (f"\nDescending order: {thirdNum}, {secondNum}, {fourthNum}, {firstNum} \n")
elif thirdNum > fourthNum > firstNum > secondNum:
    print (f"\nDescending order: {thirdNum}, {fourthNum}, {firstNum}, {secondNum} \n")
elif thirdNum > fourthNum > secondNum > firstNum:
    print (f"\nDescending order: {thirdNum}, {fourthNum}, {secondNum}, {firstNum} \n")

# six (6) possible results if the fourth number is the highest number
elif fourthNum > firstNum > secondNum > thirdNum:
    print (f"\nDescending order: {fourthNum}, {firstNum}, {secondNum}, {thirdNum} \n")
elif fourthNum > firstNum > thirdNum > secondNum:
    print (f"\nDescending order: {fourthNum}, {firstNum}, {thirdNum}, {secondNum} \n")
elif fourthNum > secondNum > firstNum > thirdNum:
    print (f"\nDescending order: {fourthNum}, {secondNum}, {firstNum}, {thirdNum} \n")
elif fourthNum > secondNum > thirdNum > firstNum:
    print (f"\nDescending order: {fourthNum}, {secondNum}, {thirdNum}, {firstNum} \n")
elif fourthNum > thirdNum > firstNum > secondNum:
    print (f"\nDescending order: {fourthNum}, {thirdNum}, {firstNum}, {secondNum} \n")
elif fourthNum > thirdNum > secondNum > firstNum:
    print (f"\nDescending order: {fourthNum}, {thirdNum}, {secondNum}, {firstNum} \n")
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

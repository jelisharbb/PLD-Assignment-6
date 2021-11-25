# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# greetings to the user
print ("\nWelcome to Jelisha's Addition Quiz! \nThis is a ten (10) item quiz that will test your mathematical skills in adding random numbers from 0 to 99.")

userName = input("\nPlease enter your name:\n")

# ask if the user is ready or not using while loops
userReady = input(f"\nHey, {userName}! Are you ready to take the quiz? (Answer: Yes or No)\n")
ready = False

while not ready:
    if userReady.replace(".","",1).title() == "Yes" or userReady.replace("!","",1).title() == "Yes":
        ready = True
    while userReady.title() != "Yes":     
        if userReady.title() == "No":
            userReady = input(f"\nIt's okay, {userName}. Take your time in pulling yourself together. \n\nAre you ready now to take the quiz? \n")
            if userReady.title() == "Yes":
                break
            elif userReady.title() == "No":
                break
        else:
            userReady = input(f"\nHey, {userName}. This program cannot read your input. Please try again by answering Yes or No.\n\nAre you ready now to take the quiz? \n")
            if userReady.title() == "No":
                break
            elif userReady.title() == "Yes":
                break
print("\n\nYey! Let's start!\n")

# generating random numbers
from random import randrange

# variables to be used
number = 1
items = 10
correct = 0
wrong = 0

# addition quiz starts here
while number <= items:
    firstNum = randrange (0,99)
    secondNum = randrange (0,99)
    systemAns = firstNum + secondNum
    if number <= items:
        print (f"\nQuestion no. {number}: {firstNum} + {secondNum}")
        userAns = input("\nEnter you answer here: ")

        # if the user entered a numerical input
        if userAns.isdigit() == True:

            # if the user is correct
            if int(userAns) == systemAns:
                correct += 1
                number += 1
                if correct <= 3:
                    print (f"Correct! Good job, {userName}.")
                elif correct > 3 and correct <= 6:
                    print (f"Correct! You are amazing, {userName}.")
                elif correct > 6 and correct <= 9:
                    print ("Wow! You are great!")
                elif correct == 10:
                    None

            # if the user is wrong
            elif userAns != systemAns:
                wrong += 1
                number += 1
                if wrong <= 3:
                    print (f"Nice try, {userName}. The correct answer is {systemAns}.")
                elif wrong > 3 and wrong <= 6:
                    print (f"Unfortunately, you are wrong. The correct answer is {systemAns}.")
                elif wrong > 6 and wrong <= 9:
                    print (f"The correct answer is {systemAns}. Try to focus more. You can do it, {userName}!")

        # if the user entered an alphabet
        elif userAns.isalpha() == True:
            print (f"Hey, {userName}. Please provide numerical input only.")

        else:
            print (f"Hey, {userName}. Please provide numerical input only.")

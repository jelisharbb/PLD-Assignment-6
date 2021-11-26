# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# greetings to the user
print ("\nWelcome to \033[1mJelisha's Addition Quiz!\033[0m \nThis is a ten (10) item quiz that will test your mathematical skills in adding random numbers from 0 to 99.")

userName = input("\nPlease enter your \033[95mname:\033[0m\n")

# ask if the user is ready or not using while loops
userReady = input(f"\nHey, \033[4m{userName.title()}\033[0m! Are you ready to take the quiz? (Answer: Yes or No)\n")
ready = False

while not ready:
    if userReady.replace(".","",1).title() == "Yes" or userReady.replace("!","",1).title() == "Yes":
        ready = True
    while userReady.title() != "Yes":     
        if userReady.title() == "No":
            userReady = input(f"\nIt's okay, \033[4m{userName.title()}\033[0m. Take your time in pulling yourself together. \n\nAre you ready now to take the quiz? \n")
            if userReady.title() == "Yes":
                break
            elif userReady.title() == "No":
                break
        else:
            userReady = input(f"\nHey, \033[4m{userName.title()}\033[0m. This program \033[91mcannot\033[0m read your input. Please try again by answering \033[4mYes or No\033[0m.\n\nAre you ready now to take the quiz? \n")
            if userReady.title() == "No":
                break
            elif userReady.title() == "Yes":
                break
print("\n\n\033[102m\033[30mYey! Let's start!\033[0m\n")

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
        print (f"\nQuestion no. {number}: \033[96m{firstNum} + {secondNum}\033[0m")
        userAns = input("\nEnter you \033[95manswer\033[0m here: ")

        # if the user entered a numerical input
        if userAns.isdigit() == True:

            # if the user is correct
            if int(userAns) == systemAns:
                correct += 1
                number += 1
                if correct <= 3:
                    print (f"\033[92mCorrect! Good job, {userName.title()}.\033[0m")
                elif correct > 3 and correct <= 6:
                    print (f"\033[92mCorrect! You are amazing, {userName.title()}.\033[0m")
                elif correct > 6 and correct <= 9:
                    print ("\033[92mWow! You are great!\033[0m")
                elif correct == 10:
                    print ("\033[92mPerfect!\033[0m")

            # if the user is wrong
            elif userAns != systemAns:
                wrong += 1
                number += 1
                if wrong <= 3:
                    print (f"\033[91mNice try, {userName}. The correct answer is \033[1m{systemAns}.\033[0m")
                elif wrong > 3 and wrong <= 6:
                    print (f"\033[91mUnfortunately, you are wrong. The correct answer is \033[1m{systemAns}.\033[0m")
                elif wrong > 6 and wrong <= 9:
                    print (f"\033[91mThe correct answer is \033[1m{systemAns}.\033[0m \033[91mTry to focus more. You can do it, {userName}!\033[0m")

        # if the user entered an alphabet
        elif userAns.isalpha() == True:
            print (f"Hey, \033[4m{userName.title()}\033[0m. Please provide \033[4mnumerical\033[0m input only.")

        else:
            print (f"Hey, \033[4m{userName.title()}\033[0m. Please provide \033[4mnumerical\033[0m input only.")

# total scores
if correct == 10 and wrong == 0:
    print (f"\n\033[93mCongratulations, {userName.title()}! You got a score of {correct}/{items}.\033[0m\n")
elif correct >= 6 and correct <= 9:
    print (f"\n\033[93mYou did a great job, {userName.title()}! You got a score of {correct}/{items}.\033[0m\n")
elif correct >= 3 and correct <= 5:
    print (f"\n\033[93mYou are cool, {userName.title()}. You got a score of {correct}/{items}.\033[0m\n")
else:
    print (f"\n\033[93mNice try, {userName.title()}. You got a score of {correct}/{items}.\033[0m\n")
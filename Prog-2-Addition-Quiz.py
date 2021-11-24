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
print("\nYey! Let's start!\n")
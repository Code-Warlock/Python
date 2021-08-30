import random
number = random.randint(1,2)
guess = int(input("Enter the number you want to guess(1-2) : "))
guesses = 0
lives = 3
while lives > 1:
    if guess < number:
        lives -= 1
        print("Wrong Try again!\nThe correct answer was "+ str(number) + "\nYou have " + str(lives) + " lives left")
        number = random.randint(1,2)
        guess = int(input("Enter the number you want to guess(1-2) : "))
    elif guess > number:
        lives -= 1
        print("You got it wrong\nThe correct answer was "+str(number) + "\nYou have " + str(lives) + " lives left")
        number = random.randint(1,2)
        guess = int(input("Enter the number you want to guess(1-2) : "))
    elif guess == number:
        if abs(3-lives) == 1:
            print("Correct!\nYou got it right after " + str(abs(3-lives)) + " trial")
        else:
            print("Correct!\nYou got it right after " + str(abs(3-lives)) + " trials")
        break
else:
    if guess == number:
        if abs(3-lives) == 1:
            print("Correct!\nYou got it right after " + str(abs(3-lives)) + " trial")
        else:
            print("Correct!\nYou got it right after " + str(abs(3-lives)) + " trials")
    else:
        print("The correct answer was " + str(number) +"\nGame Over\nNo life left")

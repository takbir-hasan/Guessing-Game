# Guessing Game in Python
# Author Takbir Hasan

from random import randint
continueGame = 1
while(continueGame):
    guessNumber= int(input("Enter a new number from 1 to 10 : "))
    resultNumber= randint(1,10)

    if guessNumber==resultNumber:
        print("Congratulations! You Won.")
        continueGame = 0
    else:
        print("Sorry! You Lost.")
        print("The Correct Guess is: ",resultNumber)
        print("You can get another chance untill you guess a correct number.\n")
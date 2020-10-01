import random
import os

gamecycle = True
guesses = 0
arraything = ["+", "-"]
print("Welcome to the Very Hard Number Guesser!")
while True:
    hardlvl = int(input("Input hardness level (minimum is 5)> "))
    if hardlvl < 5:
        print("Level lower than 5. Try again.")
        hardlvl = int(input("Input hardness level (minimum is 5)> "))
    else:
        break 

numbermax = int(input("What should be the highest number to guess?> "))
number = random.randint(1, numbermax)
while gamecycle:
    guess = int(input("What is your guess?> "))
    if guess > number:
        os.system("cls")
        print(f"Your guess is too high by {guess - number}.")
        exec(f"number = number {''.join(random.choice(arraything))} random.randint(5, hardlvl)")
        guesses += 1
    elif guess < number:
        os.system("cls")
        print(f"Your guess is too low by {number - guess}.")
        exec(f"number = number {''.join(random.choice(arraything))} random.randint(5, hardlvl)")
        guesses += 1
    elif guess == number:
        print(f"You guessed it! Took you {guesses} guesses.\n")
        input("Press Enter to exit...")
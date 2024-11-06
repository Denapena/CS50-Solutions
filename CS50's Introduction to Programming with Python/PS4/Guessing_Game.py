# Guessing Game

from random import randint

while True:
    try:
        level = int(input("Please select the level (number): "))
        if level >= 1:
            break
        else:
            print("It needs to be a positive integer, try again!")
    except ValueError:
        print("Wrong input, number neccessary, try again!")

number = randint(1,level)
print(f"Now try to guess the number we imagined which is in rage 1 - {level}")

while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just right!")
            break
        elif guess < number:
            print("Too small!")
        else:
            print("Too large")
    except ValueError:
        print("Wrong input, number neccessary, try again!")

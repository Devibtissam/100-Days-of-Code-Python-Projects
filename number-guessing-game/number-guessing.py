import random
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10



def check_number(number, correct_number,turns):
    if number > correct_number:
        print("Too high")
        return turns - 1
    elif number < correct_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it!!! The answer was {number}")

def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard':").lower()
    if level=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
        



def game():
    print(logo)


    print("Welcome to The Guessing Numer Game!")
    print("I'm thinking of a Number between 1 and 100.")


    correct_number = random.randint(1, 101)

    turns = set_difficulty()
    guess = 0
    while guess!=correct_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        turns=check_number(guess, correct_number,turns)

        if turns==0:
            print("You've run out of guesses, you lose.")
            return

game()

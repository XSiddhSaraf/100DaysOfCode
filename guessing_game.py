# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art1 import guessing_logo
from random import randint

print(guessing_logo)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

is_stop = False
while not is_stop:

    choice = input("Choose a difficulty. Type 'easy' or 'hard':")

    if choice == 'hard':
        attempt = 5
        print('You have 5 attempts remaining to guess the number.')
        while attempt > 0:
            guess = int(input('Make a aguess: '))
            if guess < answer:
                print('Too low!')
                print('Guess again')

            elif guess > answer:
                print('Too high!')
                print('Guess again')

            else:
                print(f"You got it! The answer was {answer}")
            attempt -= 1
            print(
                f'You have {attempt} attempts remaining to guess the number.')

    elif choice == 'easy':
        attempt = 10
        print('You have 10 attempts remaining to guess the number.')
        while attempt > 0:
            guess = int(input('Make a aguess: '))
            if guess < answer:
                print('Too low!')
                print('Guess again')

            elif guess > answer:
                print('Too high!')
                print('Guess again')

            else:
                print(f"You got it! The answer was {answer}")
                break
            attempt -= 1
            print(
                f'You have {attempt} attempts remaining to guess the number.')

    else:
        print("Invalid choice !! Please choose between 'easy' or 'hard'.")

    to_contiue = input("Do you want to continue? Type 'yes' for that.")
    if to_contiue.lower() == 'yes':
        is_stop = False
    else:
        is_stop = True

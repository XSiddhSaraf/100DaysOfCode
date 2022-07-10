############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from os import system, name
from time import sleep
from art1 import blackjak_logo


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw :)"
    elif comp_score == 0:
        return "You lost. Oponent has Blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You loose."
    elif comp_score > 21:
        return "Opponent went over.You win."
    elif user_score > comp_score:
        return "You win"
    else:
        return "You loose."


def play_game():

    print(blackjak_logo)

    user_cards = []
    computer_cards = []
    is_game_over = False
    # Dealing cards for computer
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    # Dealing cards for user
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and final score is {user_score}")
    print(
        f"Computer's final hand is {computer_cards} and final score is {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    sleep(2)
    clear()
    play_game()

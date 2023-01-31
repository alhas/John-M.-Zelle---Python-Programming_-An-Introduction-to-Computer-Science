# TODO All Face cards are 10 point. J,Q,K, Ace has 1 and 11 value depends on the hand.
# TODO Input function to how many times program run.
# TODO Draw Card Function - generate 10 deck of cards and shuffle it then return values in step.
# TODO Player Function
# TODO Dealer Function
# TODO Tournament Function
# TODO Probability Function
import random

BLACK_JACK = 21
SOFT_HAND = 17


def input():
    inp = int(input("How many times do you want to play?: "))
    return inp


def tournament():
    pass


def player():

    hand = 0
    player_card = draw_card()

    while hand <= BLACK_JACK:
        if type(player_card[1]) == bool:
            if hand+11 < SOFT_HAND:
                hand += 11
            else:
                hand += 1
        if player_card[0] in ['J', 'Q', 'K']:
            hand += player_card[1]
        elif player_card[0]=='N':
            random.choice(player_card[1])
            hand += player_card

    return hand


def dealer():
    pass


def draw_card():
    cards = {"J": 10,
             "Q": 10,
             "K": 10,
             "A": bool,
             "N": (2, 3, 4, 5, 6, 7, 8, 9, 10)
             }

    a = random.choice(list(cards.items()))

    return a


def main():

    pass


if __name__ == "__main__":
    main()
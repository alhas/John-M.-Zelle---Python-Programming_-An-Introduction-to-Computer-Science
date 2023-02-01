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
ACE = 11


def input():
    inp = int(input("How many times do you want to play?: "))
    return inp


def tournament():
    pass


def player():

    hand = 0

    while hand <= BLACK_JACK:
        player_card = deck()
        if type(player_card) == bool:
            if hand+ACE < SOFT_HAND:
                hand += 11
            else:
                hand += 1
        hand += player_card

    return hand


def dealer():
    pass


def deck():
    cards = [True, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    a = random.choice(list(cards))

    return a


def main():

    pass


if __name__ == "__main__":
    main()

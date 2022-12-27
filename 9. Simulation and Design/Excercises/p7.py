from random import randrange


def main():
    print(f"Probablity of wining {probability()}")


def gamblerInput():
    n = int(input("How many times do you want to play? "))
    return n


def sim_dice():

    dice_one = randrange(1, 6)
    dice_two = randrange(1, 6)

    return dice_one + dice_two


def sim_roller():

    total_value = sim_dice()

    if total_value in [2, 3, 12]:

        return 0
    elif total_value in [7, 11]:
        return 1
    else:
        initial_value = total_value
        while True:
            rollagain = sim_dice()
            if rollagain == initial_value:
                return 1
            elif rollagain == 7:
                return 0


def probability():
    n = gamblerInput()
    totalWin = 0
    for _ in range(n):
        totalWin += sim_roller()

    return totalWin/n


if __name__ == "__main__":
    main()

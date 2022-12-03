from math import sqrt


def distance():

    x1 = int(input("Please enter x1: "))
    x2 = int(input("Please enter x2: "))
    y1 = int(input("Please enter y1: "))
    y2 = int(input("Please enter y2: "))

    distance = sqrt((x2-x1)**2 + (y2-y2)**2)

    print(f"Distance Is: {distance}")



distance()
from math import pi, sin


def lengthOfLadder():

    height = int(input("Height of Ladder: "))
    angle = int(input("Angle: "))
    length = height/sin(angle)
    radians = (pi/180) * angle

    print(f"The lengh is {length} the radians is {radians}")


lengthOfLadder()

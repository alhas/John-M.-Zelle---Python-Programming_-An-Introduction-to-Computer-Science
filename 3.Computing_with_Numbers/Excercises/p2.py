from math import pi


def main():

    d = float(input("Pleae enter diameter of pizza"))
    p = float(float(input("Please enter price of pizza")))

    area = pi*d

    print(f"The ratio of price and area is: {area/p}")

main()
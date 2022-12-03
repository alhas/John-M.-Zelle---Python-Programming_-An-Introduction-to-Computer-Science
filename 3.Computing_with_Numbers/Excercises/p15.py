from math import pi


def approximatesOfpi():

    print("Welcome to Pi approximation!\n")
    n = int(input("Enter the number of terms to sum: "))
    approx = 0
    sign = -1

    # -- start Gregory-Leibniz series

    for i in range(1, n+1):  # do this 'n' times
        sign *= -1
        approx += sign * ( 4 / (2*i - 1) )

    # -- end Gregory-Leibniz series

    print("Approximate value of pi is:", approx)

    difference = pi - approx


approximatesOfpi()

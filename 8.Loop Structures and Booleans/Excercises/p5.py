from math import sqrt


def prime_number_finder():

    n = int(input("Please enter your number: "))

    if n >= 2:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return print(f"{n} is not prime.")
            else:
                return print(f"{n} is prime number.")


prime_number_finder()

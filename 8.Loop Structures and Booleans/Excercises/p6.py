from math import sqrt


def prime_number_finder(n):

    if n >= 2:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
            else:
                return True


n = int(input("Please enter your number: "))
for i in range(n+1):
    if prime_number_finder(i):
        print(i)

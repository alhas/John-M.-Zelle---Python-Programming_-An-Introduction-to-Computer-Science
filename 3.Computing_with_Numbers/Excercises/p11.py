
def sumOfNumbers():

    n = int(input("Enter number: "))

    num = 0
    for i in range(n+1):
        num += i
    print(f"sum of numbers is {num}")


sumOfNumbers()

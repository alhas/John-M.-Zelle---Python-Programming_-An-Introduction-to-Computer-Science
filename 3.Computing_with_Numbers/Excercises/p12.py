
def sumOfCubes():

    n = int(input("Enter number: "))

    num = 0
    for i in range(1,n+1):
        num += i**3
    print(f"sum of numbers is {num}")


sumOfCubes()

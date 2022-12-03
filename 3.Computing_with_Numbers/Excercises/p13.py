

def sumSeriesOfNumbers():

    series = int(input("Enter how many numbers you will sum: "))

    total = 0
    for i in range(1,series+1):
        int(input("Please enter number: "))
        print(i)
        total += i
        print(f"Total Number is now: {total}")


sumSeriesOfNumbers()
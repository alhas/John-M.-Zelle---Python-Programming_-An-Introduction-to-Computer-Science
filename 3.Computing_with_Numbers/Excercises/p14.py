def avarageSumOfNumbers():

    series = int(input("Enter how many numbers you will sum: "))

    total = 0
    for i in range(1,series+1):
        int(input("Please enter number: "))
        total += i
        print(f"Avarage is now: {total/series}")


avarageSumOfNumbers()
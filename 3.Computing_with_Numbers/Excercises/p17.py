

def sqrt(x, tolerance):
    guess = x / 2

    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess)/2

        return guess

x = int(input("Enter a number: "))
tolerance = float(input("Enter the tolerance: "))
print("The square root of", x, "is approximately", sqrt(x, tolerance))

    

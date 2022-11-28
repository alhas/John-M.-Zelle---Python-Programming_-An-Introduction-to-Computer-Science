# A program to compute the value of an investment
# carried 10 years into the future
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter Number of Years for Investment: "))
    for i in range(years):
        principal = principal * (1 + apr)
    print("The value in 10 years is: ", principal)

main()

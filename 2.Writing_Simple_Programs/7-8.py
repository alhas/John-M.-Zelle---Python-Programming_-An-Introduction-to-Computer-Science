# A program to compute the value of an investment
# carried 10 years into the future
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    invest = eval(input("Enter the your investment: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    periods = eval(
        input("Enter number of times that the interest is compounded."))
    years = eval(input("Enter Number of Years for Investment: "))
    for i in range(years):
        nominal = years * periods + (apr/periods)
        invest = invest * years
        principal = principal * (1 + apr)
    print("The value in 10 years is: ", principal)
    print(nominal)

main()

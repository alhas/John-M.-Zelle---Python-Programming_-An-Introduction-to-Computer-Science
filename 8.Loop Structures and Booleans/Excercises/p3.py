

def invenstment_calculation():

    annualInterest = float(input("Please enter yearly interest rate: "))
    investment = float(input("Please enter your investment: "))

    years = 0
    initialInvestment = investment
    r = annualInterest/100

    while investment < initialInvestment*2:
    
        investment = investment * (1 + r)
        years += 1
    print(investment)
    print(f"Your investment will be double in {years} years.")


invenstment_calculation()



def gregorianEpact():
    
    year = int(input("Please enter year for Gregorian Epact: "))
    C = year//100

    epact = (8+(C//4)-C+((8*C+13)//25)+11*(year % 19)) % 30

    print(f"The epact is= {epact}")


gregorianEpact()

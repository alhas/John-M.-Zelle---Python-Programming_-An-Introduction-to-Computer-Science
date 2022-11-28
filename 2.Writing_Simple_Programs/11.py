def calc():
    print("this is a calculator")
    while 1:
        calculation = eval(input("Please enter your calculation: "))
        print(calculation)
        
        decision = eval(input("If you want to continue calculation press 1: "))
        if decision != 1:
            break


calc()
def wage():

    week_hours = 40
    wage = 0
    rate = float(input("Please Enter Hourly Rate: "))
    worked_hours = float(input("Please Enter Worked Hours (Can be max 60h): "))

    try:
        wage = worked_hours * rate
        if worked_hours > 40 and worked_hours <= 60:
            extra_hours = worked_hours - week_hours
            wage = extra_hours * 1.5 + wage
        else:
            print("Worked Hours can't be more than 60")
    except ValueError:
        print("You typed wrong value. ")

    print(f"Your weekly wage is {wage}, and your Mounthly wage is: {wage*4}")


wage()

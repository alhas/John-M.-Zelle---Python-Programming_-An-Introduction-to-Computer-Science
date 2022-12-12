def grade():

    point = int(input("Enter Grade: "))
    grade_list = ["A", "B", "C", "D", "F", "F"]

    if point <= 5:

        for i in range(len(grade_list)):
            if point == i:
                grade_list.reverse()
                return print(grade_list[i])


"""  
    #Solution 2
    if point <= 5:

        if point == 5:
            print(grade_list[grade_list.index("A")])
        elif point == 4:
            print(grade_list[grade_list.index("B")])
        elif point == 3:
            print(grade_list[grade_list.index("C")])
        elif point == 2:
            print(grade_list[grade_list.index("D")])
        else:
            print("F")
    else:
        print("Please enter value between 0 to 5: ")
"""
grade()

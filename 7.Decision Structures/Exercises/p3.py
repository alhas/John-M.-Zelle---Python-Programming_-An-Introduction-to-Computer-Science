def point_to_grede():
    point = int(input("Please enter student's grade: "))

    letters = [[90, 100, "A"], [80, 89, "B"],
               [70, 79, "C"], [60, 69, "D"], [0, 59, "F"]]

    if point <= 100:
        i = 0
        for g in letters:
            for a in range(len(letters)):
                if point >= letters[a][0] and point <= letters[a][1]:
                    return print(letters[a][2])

    else:
        return print("!!! Please enter numbers between 100 and 0 !!!")


"""    if point <= 100:
        if point >= 90 and point <= 100:
            print("A")
        elif point >= 80 and point <= 89:
            print("B")
        elif point >= 70 and point <= 79:
            print("C")
        elif point >= 60 and point <= 69:
            print("D")
        else:
            print("F")
    else:
        print("Please enter numbers between 0 and 100")
 """

point_to_grede()

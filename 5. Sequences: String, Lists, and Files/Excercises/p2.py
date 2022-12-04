def grade():

    point = int(input("Please enter student's grade: "))

    scale = ["F", "F", "D", "C", "B", "A"]
    grade = scale[point]

    print("Students grade is {0}-{1}".format(point, grade))


grade()

def grade():

    point = int(input("Please enter student's grade: "))

    scale = [(90, 100, "A"),
             (80, 89, "B"),
             (70, 79, "C"),
             (60, 69, "D"),
             (0, 59, "F")]

    for min_score, max_score, grade in scale:

        if min_score <= point < max_score:

            print("Students grade is {0}-{1}".format(point, grade))

grade()

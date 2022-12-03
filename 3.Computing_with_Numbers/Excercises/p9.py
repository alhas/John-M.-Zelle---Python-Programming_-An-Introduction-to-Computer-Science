from math import sqrt


def areaOfTriangle():

    a = int(input("Please enter side a: "))
    b = int(input("Please enter side b: "))
    c = int(input("Please enter side c: "))

    s = (a+b+c)//2

    A = sqrt(s*(s-a)*(s-b)*(s-c))

    print(f"Area of triangle is: {A}")


areaOfTriangle()

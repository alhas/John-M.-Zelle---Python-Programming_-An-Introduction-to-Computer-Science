def syracuse():

    x = int(input("Please enter your Syracuse number: "))

    while x > 1:

        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x+1

        print(int(x))

syracuse()

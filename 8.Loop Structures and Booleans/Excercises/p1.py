def fibonacci(n):
    a = 1
    b = 0
    for i in range(n):

        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            c = a+b
            a = b
            b = c

    return c


print(fibonacci(6))


def recursive_fibo(n):

    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return recursive_fibo(n-1) + recursive_fibo(n-2)


print(recursive_fibo(6))

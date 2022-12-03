
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter a number: "))
print("The nth Fibonacci number is:", fibonacci(n))


def fibonacci(n):
    a = 1
    b = 1
    for i in range(3, n+1):
        c = a + b
    return b


n = int(input("Enter a number: "))
print("The nth Fibonacci number is:", fibonacci(n))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    if n % 2 != 0:
        print("Number must be even")
        return None

    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return (i, n - i)

def main():
    n = int(input("Enter an even number: "))
    primes = find_primes(n)
    if primes:
        print(f"{primes[0]} + {primes[1]} = {n}")
    else:
        print("No such primes found")

if __name__ == "__main__":
    main()

"""
This is an example for creating and using a generator
"""


def fibonacci(limit=25):
    a, b = -1, 1
    for n in range(limit):
        c = a + b
        a, b = b, c
        yield c


def primes(upto = 100):
    def is_prime(n):
        if n <= 1: return False
        if n in (2, 3): return True

        d = 2
        limit =  n//2
        while d <= limit:
            if n % d == 0: return False
            d += 1
        return True

    for num in range(1, upto+1):
        if is_prime(num):
            yield num


def main():
    for f in fibonacci(10):
        print(f, end=', ')
    print()

    for p in primes(25):
        print(p, end=', ')


if __name__ == '__main__':
    main()

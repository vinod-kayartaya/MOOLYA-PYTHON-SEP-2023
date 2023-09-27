"""
This is an example for understanding the `range` object and using the `for` loop with it
"""


def main():
    r = range(10)  # creating an object of the `range` class
    for n in r:
        print(n, end=', ')

    print()

    for n in range(11, 21):  # represents a generator that can give numbers between 11 and 20
        print(n, end=', ')

    print()

    for n in range(0, 101, 10):
        print(n, end=', ')

    print()

    for n in range(10, 0, -1):
        print(n, end=', ')

    print()


if __name__ == '__main__':
    main()


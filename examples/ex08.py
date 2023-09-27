"""
This script accepts a number from the user (n >= 1)
and prints the same number of fibonacci series elements.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....

For example, if the input is 7, then the first 7 elements in the series are the output:

0, 1, 1, 2, 3, 5, 8
"""


def main():
    n = int(input('Enter a number >=1 : '))
    n1, n2 = -1, 1
    while n >= 1:
        f = n1 + n2
        print(f, end=', ')
        n1, n2 = n2, f
        n -= 1


if __name__ == '__main__':
    main()

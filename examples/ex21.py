"""
This example illustrates the use of command line arguments and exception handling
"""
import sys


def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        num = int(arg1)
        den = int(arg2)

        quot = num // den
        rem = num % den

        print(f'{num} divided by {den} results into a quotient of {quot} and remainder of {rem}')
    except (IndexError, ValueError):
        print('You must supply 2 integers')
    except ZeroDivisionError:
        print('2nd number cannot be zero')

    print('end of main()')


if __name__ == '__main__':
    main()

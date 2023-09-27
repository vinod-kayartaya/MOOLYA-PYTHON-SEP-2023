"""
This is an example of using `for` loop with a bunch of values (lists, tuples or sets)
"""


def main():
    for name in 'Vinod', 'Shyam', 'Harish', 'Ramesh':
        print(name, end=', ')
    print()

    for name in ['Vinod', 'Shyam', 'Harish', 'Ramesh']:
        print(name, end=', ')
    print()

    for name in ('Vinod', 'Shyam', 'Harish', 'Ramesh'):
        print(name, end=', ')
    print()

    for name in {'Vinod', 'Shyam', 'Harish', 'Vinod', 'Ajay', 'Vinod', 'Rohit', 'Shyam'}:
        print(name, end=', ')
    print()


if __name__ == '__main__':
    main()

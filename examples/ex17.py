"""
Example of tuples

A `tuple` is a read-only collection.
Has only two methods -> count, index
"""


def main():
    t1 = 10, 20, 30, 40
    print(f't1 is {t1} and type of t1 is {type(t1)}')

    t2 = (12, 34, 56)
    print(f't2 is {t2}')

    print(f'first element in t1 is {t1[0]} and last is {t1[-1]}')
    print(f'index of 30 in t1 is {t1.index(30)}')

    # print(f'index of 300 in t1 is {t1.index(300)}')  # ValueError is raised, since there is no 300
    if 300 in t1:
        print(f'index of 300 in t1 is {t1.index(300)}')

    t3 = (120, )
    print(f'type of t3 is {type(t3)}')


if __name__ == '__main__':
    main()

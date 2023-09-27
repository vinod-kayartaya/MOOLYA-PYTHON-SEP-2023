def line():
    print('-' * 80)


def main():
    n1, n2, n3 = 102, 22, 34
    print(f'n1 = {n1}, n2 = {n2} and n3 = {n3}')

    print(f'n1 / n2 is {n1/n2}')
    print(f'n1 // n2 is {n1 // n2}')
    print(f'n1 % n2 is {n1 % n2}')

    print('vinod' * 5)
    n3 += 100
    print(f'after adding 100 to n3, n3 is {n3}')
    line()

    # relational operators:
    # < <= > >= == !=
    # logical operators:
    # and or not


if __name__ == '__main__':
    main()

def main():
    """
    This is the entry point for this script

    :return: None
    """

    num = input('Enter a number: ')
    try:
        num = float(num)
        print(f'The square of {num} is {num*num}')
    except ValueError:
        print('You were expected to enter only a number.')


if __name__ == '__main__':
    main()

def main():
    name = 'vinod'
    print(f'name.startswith("vin") is {name.startswith("vin")}')
    print(f'name.endswith("vin") is {name.endswith("vin")}')

    num = input('Enter a number: ')
    if not num.isnumeric():
        print(f'"{num}" is not a number. Please try again')
    else:
        num = float(num)
        print(f'square of {num} is {num*num}')


if __name__ == '__main__':
    main()

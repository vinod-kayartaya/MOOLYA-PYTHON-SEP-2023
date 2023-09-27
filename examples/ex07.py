def main():
    total = 0
    count = 0
    while True:
        num = input('Enter a number (0 to stop): ')
        if not num.isnumeric():
            continue  # skips the rest of the loop body, and starts all over again from the start of loop

        num = float(num)

        if num == 0:
            break  # skips the rest of the loop body, and exits the loop

        total += num
        count += 1

    print(f'number of numeric inputs = {count}')
    print(f'sum of numeric inputs = {total}')
    print(f'average of numeric inputs = {total/count}')


if __name__ == '__main__':
    main()

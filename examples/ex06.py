def main():
    dt = input('Enter date in dd/mm/yyyy format: ')

    if dt.count('/') != 2:
        print('Invalid date. Must be in dd/mm/yyyy format')
        return

    d, m, y = dt.split('/')
    # if d.isdigit() is False or m.isdigit() is False or y.isdigit() is False:
    if not (d.isdigit() and m.isdigit() and y.isdigit()):
        print('Invalid date.')
        return

    d = int(d)
    m = int(m)
    y = int(y)

    if y > 9999:
        print('Year must be <= 9999')
        return

    if m < 1 or m > 12:
        print('Month must be between 1 and 12')
        return

    max_days = 31
    if m in (4, 6, 9, 11):
        max_days = 30
    elif m == 2:
        max_days = 29 if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 28

    if d > max_days:
        print(f'Date must be between 1 and {max_days}')
        return

    print('The given date is VALID!')


if __name__ == '__main__':
    main()

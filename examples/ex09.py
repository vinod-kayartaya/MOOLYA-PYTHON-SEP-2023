"""
Accept 2 numbers for `month` and `year` and print the calendar for the same in Unix's `cal` command's format:


For example for the inputs 9 and 2023, the output should be like this:

   September 2023
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30

"""

import datetime


def main():
    m = int(input('Enter a month: '))
    y = int(input('Enter a year: '))

    print(" Su Mo Tu We Th Fr Sa")

    week_day = datetime.date(y, m, 1).weekday()
    max_days = (datetime.date(y, m+1, 1) - datetime.timedelta(days=1)).day

    if week_day == 6:
        week_day = 0
    else:
        week_day += 1

    n = 1
    while n <= week_day:
        print('   ', end='')
        n += 1

    d = 1
    while d <= max_days:
        print(f'{d:3}', end='')
        if (d+week_day) % 7 == 0:
            print()
        d += 1


if __name__ == '__main__':
    main()

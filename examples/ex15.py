"""
This is an example for understanding list comprehension
"""


def main():
    nums = [903, 692, 894, 611, 732, 387, 577, 947, 102, 373]

    # create a new list consisting of only even numbers from the list `nums`
    even_nums = []
    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)

    print(f'even numbers from `nums` is {even_nums}')

    # using list comprehension, there is no loop or iteration
    odd_nums = [n for n in nums if n % 2]
    print(f'odd numbers from `nums` is {odd_nums}')

    squares = [n*n for n in nums]
    print(f'square of all numbers from `nums` are {squares}')

    halves = [n/2 for n in nums]
    print(f'half of each number from `nums` are {halves}')

    names = ['vinod KUMAR', 'Ramesh iyer', 'Suraj KHANNA', 'RAVI KUMAR']
    names = [name.title() for name in names]
    print(f'names in title case are {names}')

    names_without_vowels = [remove_vowels(name).upper() for name in names]
    print(f'names without vowels are {names_without_vowels}')


def remove_vowels(text):
    text = text.replace(' ', '_')
    return ''.join([c for c in text if c.lower() not in ('a', 'e', 'i', 'o', 'u')])


if __name__ == '__main__':
    main()

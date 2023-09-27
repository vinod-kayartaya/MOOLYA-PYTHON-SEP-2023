"""
Example to understand functions (user defined)
"""


def say_hello(name=None, city=None):
    name = 'friend' if name is None else name
    city = 'your city' if city is None else city

    print(f'Hello, {name}! How\'s weather in {city}?')


def calculate_sum(*args):
    return sum([n for n in args if type(n) in (int, float)])


def full_name(**kwargs):
    # print(f'kwargs is of type {type(kwargs)}')
    # print(f'kwargs is {kwargs}')
    first = kwargs.get('first')
    if first is None:
        return 'Nobody'

    last = kwargs.get('last', '')
    gender = kwargs.get('gender', 'Male')

    title = 'Mr' if gender == 'Male' else 'Ms'

    return f'{title}.{first} {last}'









def main():
    say_hello()
    say_hello('Vinod')
    say_hello(city='Bangalore')
    say_hello('Vinod', 'Bangalore')
    say_hello(city='Chennai', name='Ravi')

    total = calculate_sum(10, 20, 123, 49, 'vinod', False, 29.3, 33)
    print(f'total is {total}')

    name = full_name(first='Vinod', last='Kumar', gender='Male')
    print(f'name is {name}')
    name = full_name(first='Vinod', lastname='Kumar', gender='Male')
    print(f'name is {name}')
    name = full_name(first='Suma', gender='Female')
    print(f'name is {name}')
    name = full_name(first='Ravi', last='Rao')
    print(f'name is {name}')
    name = full_name()
    print(f'name is {name}')


if __name__ == '__main__':
    main()

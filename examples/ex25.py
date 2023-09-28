def say_hello():
    print('hello, world!')


def say_hello(name, city):
    print(f'hello {name}, how\'s weather in {city}')


def main():
    a = 100
    a = 200
    print(f'a is {a}')
    say_hello('John', 'Dallas')
    say_hello()  # this will cause an error, since the 2nd method has replaced the 1st method in memory


if __name__ == '__main__':
    main()

class Parent:

    def say_hello(self):
        print('hello, world')


class Child(Parent):

    def say_hello(self, name):
        print(f'hello, {name}')


def main():
    c1 = Child()
    c1.say_hello('Vinod')
    c1.say_hello()  # this method from the Parent has been replaced in the Child class


if __name__ == '__main__':
    main()

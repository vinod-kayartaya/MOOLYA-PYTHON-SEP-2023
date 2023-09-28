"""
This is an example of OOP
"""


class Person:

    def __init__(self, name=None, city=None):
        self.name = name
        self.city = city

    def print_info(self):
        print(f'Name = {self.name}, city = {self.city}')


def main():
    p1 = Person('Vinod', 'Bangalore')  # p1 is a reference to an object of class Person
    print(f'type of p1 is {type(p1)}')
    print(f'p1 is {p1}')
    p1.print_info()

    p2 = Person()
    p2.name = 'Shyam'
    p2.city = 'Shivamogga'
    p2.print_info()


if __name__ == '__main__':
    main()

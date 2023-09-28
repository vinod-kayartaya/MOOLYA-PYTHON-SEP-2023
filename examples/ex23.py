"""
This example illustrates encapsulation in Python
"""


class Person:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__age = kwargs.get('age')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a str')
        if value.strip() == '':
            raise ValueError('name cannot be blank')
        if len(value.strip()) < 3:
            raise ValueError('name must contain at least 3 letters')

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) is not int:
            raise TypeError('age must be int')
        if value < 1 or value > 120:
            raise ValueError('age must be between 1 and 120')

        self.__age = value

    def __str__(self):
        return f'Person(name="{self.__name}", age={self.__age})'

    def print_info(self):
        print(f'Name     : {self.name}')
        print(f'Age      : {self.age} years')


def main():
    p1 = Person(name='Vinod', age=50)
    p2 = Person()

    print(p1)
    print(p2)

    p2.name = 'rajesh'
    p2.age = 33

    print(f'{p2.name} is {p2.age} years old')


if __name__ == '__main__':
    main()






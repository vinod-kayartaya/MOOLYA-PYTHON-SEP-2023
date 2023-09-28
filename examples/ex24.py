"""
This example helps us understand inheritance
"""

from ex23 import Person


class Student(Person):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__subject = kwargs.get('subject')
        self.__gpa = kwargs.get('gpa')

    def __str__(self):
        return f'Student(name="{self.name}", age="{self.age}", subject="{self.__subject}", gpa={self.__gpa})'

    def __lt__(self, other):  # automatically implies the __gt__ also
        return self.__gpa < other.__gpa

    def __le__(self, other):  # automatically implies the __ge__ also
        return self.__gpa <= other.__gpa

    def __iadd__(self, other):
        self.name += other
        return self

    # this is an example of method overriding
    def print_info(self):
        super().print_info()
        print(f'GPA      : {self.__gpa}')
        print(f'Subject  : {self.__subject}')


def main():
    s1 = Student(name='Ravi', age=33, subject='Maths', gpa=4.9)
    s2 = Student(name='Rajesh', age=23, subject='Maths', gpa=4.5)

    s1 += ' Shankar'

    print(f's1 is {s1}')
    s1.print_info()

    print(f's2 <= s1 is {s2 <= s1}')
    print(f's2 >= s1 is {s2 >= s1}')


if __name__ == '__main__':
    main()

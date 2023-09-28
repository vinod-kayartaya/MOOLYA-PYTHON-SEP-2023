"""
This is an example of polymorphism, abstract classes and abstract methods
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_shape_name(self) -> str:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Triangle(Shape):

    def __init__(self, base: float = 1.0, height: float = 1.0) -> None:
        self.__base = base
        self.__height = height

    def get_area(self) -> float:
        return 0.5 * self.__base * self.__height

    def get_shape_name(self) -> str:
        return 'Triangle'

    def get_perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float = 1.0) -> None:
        self.__radius = radius

    def get_area(self) -> float:
        return math.pi * self.__radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def get_shape_name(self) -> str:
        return 'Circle'


class Car:
    pass


#  polymorphic function
def process_shape(shape: Shape) -> None:
    if not isinstance(shape, Shape):
        raise TypeError(f'shape must be an object of a Shape, but got {type(shape)}')

    print(f'Area of the given {shape.get_shape_name()} is {shape.get_area()} and its perimeter is {shape.get_perimeter()}')


def main():

    def get_perimeter(self):
        return 1.0
    process_shape(Triangle(12, 23))

    Triangle.get_perimeter = get_perimeter

    # process_shape(Shape())
    process_shape(Circle(23))
    process_shape(Triangle(12, 23))
    # process_shape(Car())


if __name__ == '__main__':
    main()

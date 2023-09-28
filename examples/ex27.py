from logger_config import logger
from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print('generic animal sound...')


class Tiger(Animal):
    def make_sound(self):
        print('Grr....')


class Cat(Animal):
    def make_sound(self):
        print('Meow....')


class Dog(Animal):
    pass


class Car:
    pass


def print_animal_info(animal: Animal) -> None:
    if not isinstance(animal, Animal):
        raise TypeError(f'parameter is not an Animal instance, but of {type(animal)}')

    animal.make_sound()


def main():
    # logger.debug('this is a debug message')
    # logger.info('this is an information message')
    # logger.warning('this is a warning message')
    # logger.error('this is an error message')
    logger.critical('this is a critical message')

    # print_animal_info(Animal())  # object of abstract class
    print_animal_info(Cat())
    print_animal_info(Tiger())
    # print_animal_info(Dog())  # Dog does not override the abstract inherited method; hence abstract
    # print_animal_info(Car())  # not an Animal instance
    # print_animal_info(123)  # not an Animal instance


if __name__ == '__main__':
    main()

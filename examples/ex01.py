"""
This is an example module for testing python data types

Created by Vinod
Created on 25th Sep 2023
"""

my_name = 'Vinod'
my_age = 50
my_city = 'Bangalore'


if __name__ == '__main__':
    print('My name is %s and I am %d years old and I live in %s' % (my_name, my_age, my_city))
    print('My name is {} and I am {} years old and I live in {}'.format(my_name, my_age, my_city))
    print(f'My name is {my_name} and I am {my_age} years old and I live in {my_city}')

print(f'value of the built in variable __name__ is {__name__}')

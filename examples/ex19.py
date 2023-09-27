"""
Example to showcase different wasy of reading files
"""


def demo1():
    filename = input('Enter filename to read: ')
    file = open(filename)

    while True:
        line = file.readline()
        if line == '':
            break
        print(line, end='')

    file.close()


def demo2():
    filename = input('Enter filename to read: ')
    file = open(filename)
    content = file.read()
    print(content)

    file.close()


def demo3():
    filename = input('Enter filename to read: ')
    file = open(filename)
    lines = file.readlines()
    file.close()

    for line in lines:
        print(line, end='')


def demo4():
    filename = input('Enter filename to read: ')
    file = open(filename)
    for line in file:
        print(line, end='')

    file.close()


def demo5():
    filename = input('Enter filename to read: ')
    with open(filename) as file:
        for line in file:
            print(line, end='')

    # file.close() is automatically called here


def main():
    demo5()


if __name__ == '__main__':
    main()

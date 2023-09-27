"""
This is an example of using lists
"""


def main():
    names = list()
    names.append('Vinod')
    names.append('John')
    names.append('Kishore')
    names.insert(0, 'Suresh')
    names.insert(0, 'Rajesh')
    names.insert(0, 'Umesh')
    names.insert(100000, 'Rohit')
    print(f'names are {names}')

    name_to_remove = 'Rohit'  # change to a non-existing name and try
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f'names are {names}')
    else:
        print(f'"{name_to_remove}" could not be removed, since it does not exist in the list')

    name_popped = names.pop()
    print(f'after removing "{name_popped}", names is {names}')

    name_popped = names.pop()
    print(f'after removing "{name_popped}", names is {names}')

    name_popped = names.pop(2)
    print(f'after removing "{name_popped}", names is {names}')

    friends = ['Uday', 'Naveen', 'Satish']
    names.append(friends)
    print(f'names is {names}')
    names.pop()  # let's remove the last element, which is a list
    names.extend(friends)
    print(f'names is {names}')

    family_members = ['John', 'Jane', 'Jacob', 'Vinod', 'Vinod']
    names += family_members  # same as names.extends(family_members)

    names.sort()  # Changes the original content of the names list
    print(f'names after sorting is, {names}')

    names.reverse()  # mutates the original list
    print(f'names after reversing is, {names}')

    name_to_check = 'Vinod'
    cnt = names.count(name_to_check)
    print(f'"{name_to_check}" exists {cnt} times in the list `names`')


if __name__ == '__main__':
    main()

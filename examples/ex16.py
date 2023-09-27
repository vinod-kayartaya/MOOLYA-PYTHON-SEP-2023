"""
This is an example for understanding `dict` (dictionary)

Dictionary is a collection of values identified using keys (unlike index in a list)

"""


def main():
    d1 = dict()
    print(f'd1 is {d1}')

    d1 = dict(first_name='Vinod', last_name='Kumar', age=50, email='vinod@vinod.co')
    print(f'd1 is {d1}')

    d1 = {'title': 'Let us C', 'price': 299, 'author': 'Yashwant Kanitkar'}
    print(f'd1 is {d1}')

    print(f'the book title is "{d1["title"]}"')
    # print(f'the author of the book is "{d1["book_author"]}"')
    print(f'the author of the book is "{d1.get("author", "unknown")}"')

    print(f'the dict d1 contains these keys -> {d1.keys()}')
    print(f'the dict d1 contains these values -> {d1.values()}')

    print('following are the key/value paris in d1: ')
    for i in d1.items():
        print(i)

    keys = ['firstname', 'lastname', 'gender', 'email']
    values = ['Vinod', 'Kumar', 'Male', 'vinod@vinod.co']

    print('key/value pairs from `keys` and `values` lists: ')
    for i in zip(keys, values):
        print(i)

    d2 = dict(zip(keys, values))
    print(f'd2 is {d2}')

    d2.update(lastname='Kayartaya', middlename='Kumar', age=50)
    print(f'd2 is {d2}')


if __name__ == '__main__':
    main()

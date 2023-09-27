"""
This is an example for slice operations in a list object
"""


def main():
    nums = [903, 692, 894, 611, 732, 387, 577, 947, 102, 373]

    print(nums)
    print(nums[0])
    print(nums[5])
    print(nums[9])
    print(nums[-1])  # -1 is the last index of any list
    print(nums[-10])
    print(f'there are {len(nums)} elements in the list `nums`')
    my_name = 'Vinod Kumar Kayartaya'
    print(f'there are {len(my_name)} letters in the variable `my_name`')
    print(f'first letter in my_name is "{my_name[0]}" and the last letter in the same is "{my_name[-1]}"')

    print(f'elements between indices 3 and 7 are {nums[3:7]}')

    space_index = my_name.index(' ')
    print(f'the first name extracted from `my_name` is "{my_name[0:space_index]}"')
    print(f'the middle and the last name in `my_name` are "{my_name[space_index:].strip()}"')

    mid_index = len(nums) // 2
    print(f'first half of nums is {nums[:mid_index]}')
    print(f'second half of nums is {nums[mid_index:]}')

    print(f'elements at even indices: {nums[::2]}')
    print(f'elements at odd indices: {nums[1::2]}')
    print(f'elements of num in reverse order: {nums[::-1]}')

    print(f'reverse of "{my_name}" is "{my_name[::-1]}"')
    print(f'alternate letters in `my_name` are "{my_name[::2]}"')
    

if __name__ == '__main__':
    main()

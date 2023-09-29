def factorial(num: int) -> int:
    if type(num) is not int:
        raise TypeError('parameter must be int')

    if num <= 1:
        return 1

    f = 1
    for n in range(2, num+1):
        f *= n
    return f


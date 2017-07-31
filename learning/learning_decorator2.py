"""
Use decorator with args.
"""


def wrapper_with_args(wrapper_arg):
    """"Get wrapper args"""
    print(wrapper_arg)

    def wrapper_func(destination_func):
        return destination_func
    return wrapper_func


@wrapper_with_args('I am wrapper args')
def my_func(a, b):
    print('sum is', a + b)


my_func(2, 5)

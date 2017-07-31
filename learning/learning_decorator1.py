
"""Use decorator without args"""


def wrapper(destination_func):
    print('this is wrapper func')
    return destination_func


@wrapper
def my_func():
    print('this is my_func')


@wrapper
def sum_func(a, b):
    print('this is sum_func:', a + b)


my_func()
sum_func(2, 7)

'''Result is:
this is wrapper func
this is wrapper func
this is my_func
this is sum_func: 9
'''

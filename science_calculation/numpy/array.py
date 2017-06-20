import numpy as np


def example_1():
    """Example 1
        简单的使用numpy
    """
    a = np.array([1, 2, 3, 4])
    b = np.array((5, 6, 7, 8))
    c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])

    print(a.dtype, a)
    print(b.dtype, b)
    print(c.dtype, c)


def example_2():
    """Eample 2
        创建一个二维数组表示九九乘法表
    """

    def func2(i, j):
        return (i + 1) * (j + 1)

    func_arr = np.fromfunction(func2, (9, 9))
    print(func_arr)


example_2()

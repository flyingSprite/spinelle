import numpy as np

print(np.version.version)


class SimpleNumpyUsage(object):

    @staticmethod
    def print_array():

        print('Array: [1, 2, 3, 4]')
        print(np.array([1, 2, 3, 4]))

        print('\nArray: [[1, 2], [3, 4]]')
        print(np.array([[1, 2], [3, 4]]))

        print('\nArray: [1.2, 2, 3, 4], type: int')
        print(np.array((1.2, 2, 3, 4), dtype=np.int32))

        print('\nArray Range: np.arange(15)')
        print(np.arange(15))
        print(type(np.arange(15)))

        print('\nAuto generate 9 number from 1 to 3')
        print(np.linspace(1, 3, 9))

    @staticmethod
    def test():
        SimpleNumpyUsage.print_array()


SimpleNumpyUsage.test()

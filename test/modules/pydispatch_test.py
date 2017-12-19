# -*- coding: utf-8 -*-
"""pydispatch testing.

pip install pydispatcher
"""

from pydispatch import dispatcher


def func():
    """ Test dispatch function without arguments.

    :return: None
    """
    print('Hello World!')


dispatcher.connect(func, signal='start', sender=dispatcher.Anonymous)
dispatcher.send(signal='start')


def func2(test):
    """Test dispatch function with arguments.

    :param test: Paramater test.
    :return: None
    """
    print('Hello World!', test)


dispatcher.connect(func2, signal='second', sender=dispatcher.Anonymous)
dispatcher.send(signal='second', test='My test!')

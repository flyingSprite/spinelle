
from pydispatch import dispatcher


def func():
    print 'Hello World!'

dispatcher.connect(func, signal='start', sender=dispatcher.Anonymous)
dispatcher.send(signal='start')


"""Order 29: Open image with image url.
First, please install scikit-image

Refer to http://www.jb51.net/article/115136.htm

If install scipy failure, see https://www.youtube.com/watch?v=7GRl3gjkZN8
If has ImportError: DLL load failed, please download numpy wheel from http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
and re-install it.
"""
from skimage import io


class OpenImageWithUrl(object):

    @staticmethod
    def open(image_url):
        image = io.imread(image_url)
        io.imshow(image)
        io.show()

    @staticmethod
    def test():
        image_url = 'http://himg2.huanqiu.com/attachment2010/2017/0913/04/33/20170913043333117.jpg'
        OpenImageWithUrl.open(image_url)


# OpenImageWithUrl.test()

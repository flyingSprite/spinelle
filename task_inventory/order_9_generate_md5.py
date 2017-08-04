import hashlib


""" Order 9: Generate MD5 for text
Using utf-8 encode.

"""


class GenerateMD5(object):

    @staticmethod
    def md5(text):
        md5_hashlib = hashlib.md5()
        md5_hashlib.update(text.encode('utf8'))
        return md5_hashlib.hexdigest()


# md5_text = GenerateMD5.md5(u'123456')
# print(md5_text) # e10adc3949ba59abbe56e057f20f883e

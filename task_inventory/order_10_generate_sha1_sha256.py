import hashlib


""" Order 10: Generate SHA1 and SHA256 for text
Using utf-8 encode.

"""


class GenerateSHA(object):

    @staticmethod
    def sha1(text):
        sha1_hashlib = hashlib.sha1()
        sha1_hashlib.update(text.encode('utf8'))
        return sha1_hashlib.hexdigest()

    @staticmethod
    def sha256(text):
        sha256_hashlib = hashlib.sha256()
        sha256_hashlib.update(text.encode('utf8'))
        return sha256_hashlib.hexdigest()


# sha1_text = GenerateSHA.sha1(u'123456')
# # 7c4a8d09ca3762af61e59520943dc26494f8941b
# print(sha1_text)
#
# sha256_text = GenerateSHA.sha256(u'123456')
# # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
# print(sha256_text)

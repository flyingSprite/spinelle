import hashlib


""" Order 19: Generate SHA encryption algorithm
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512

Using utf-8 encode.

"""


class GenerateSHA(object):

    @staticmethod
    def sha1(text):
        sha1_hashlib = hashlib.sha1()
        sha1_hashlib.update(text.encode('utf8'))
        return sha1_hashlib.hexdigest()

    @staticmethod
    def sha224(text):
        sha224_hashlib = hashlib.sha224()
        sha224_hashlib.update(text.encode('utf8'))
        return sha224_hashlib.hexdigest()

    @staticmethod
    def sha256(text):
        sha256_hashlib = hashlib.sha256()
        sha256_hashlib.update(text.encode('utf8'))
        return sha256_hashlib.hexdigest()

    @staticmethod
    def sha384(text):
        sha384_hashlib = hashlib.sha384()
        sha384_hashlib.update(text.encode('utf8'))
        return sha384_hashlib.hexdigest()

    @staticmethod
    def sha512(text):
        sha512_hashlib = hashlib.sha512()
        sha512_hashlib.update(text.encode('utf8'))
        return sha512_hashlib.hexdigest()


sha1_text = GenerateSHA.sha1(u'123456')
# 7c4a8d09ca3762af61e59520943dc26494f8941b
print(sha1_text)

sha224_text = GenerateSHA.sha224(u'123456')
# f8cdb04495ded47615258f9dc6a3f4707fd2405434fefc3cbf4ef4e6
print(sha224_text)

sha256_text = GenerateSHA.sha256(u'123456')
# 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
print(sha256_text)

sha384_text = GenerateSHA.sha384(u'123456')
# 0a989ebc4a77b56a6e2bb7b19d995d185ce44090c13e2984b7ecc6d446d4b61ea9991b76a4c2f04b1b4d244841449454
print(sha384_text)

sha512_text = GenerateSHA.sha512(u'123456')
# ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413
print(sha512_text)

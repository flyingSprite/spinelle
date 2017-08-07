import rsa

""" Order 15: Using RSA to encrypt and decrypt text with public and private secret keys.

Need install rsa package, please use `pip install rsa`
"""


class UseRSA(object):

    public_pem = 'dependency/public.pem'
    private_pem = 'dependency/private.pem'

    def generate_secret_key(self):
        """Generate pulbic and private secret keys.
        :return: None
        """
        (pubkey, privkey) = rsa.newkeys(1024)
        with open(self.public_pem, 'w+') as f:
            f.write(pubkey.save_pkcs1().decode())

        with open(self.private_pem, 'w+') as f:
            f.write(privkey.save_pkcs1().decode())

    def encode_text(self, text):
        with open(self.public_pem, mode='rb') as public_file:
            keydata = public_file.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata)
        return rsa.encrypt(text.encode(encoding='utf-8'), pubkey)

    def decode_text(self, text_encode):
        with open(self.private_pem, mode='rb') as private_file:
            keydata = private_file.read()
        prikey = rsa.PrivateKey.load_pkcs1(keydata)
        return rsa.decrypt(text_encode, prikey).decode(encoding='utf-8')


# text_message = 'This is secrit message'
# use_rsa = UseRSA()
# rsa_encode_text = use_rsa.encode_text(text_message)
# print(rsa_encode_text)
# rsa_decode_text = use_rsa.decode_text(rsa_encode_text)
# # This is secrit message
# print(rsa_decode_text)
# # True
# print(text_message == rsa_decode_text)

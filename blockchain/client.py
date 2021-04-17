from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


class Client:
    def __init__(self):
        self._private_key = RSA.generate(4096)
        self._public_key = self._private_key.publickey()
        self.signer = PKCS1_v1_5.new(self._private_key)

    @property
    def client_id(self):
        return str(
            SHA256.new(self._public_key.exportKey('DER'))).encode(
                'ascii').hex()

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Random import new


class Client:
    """
    Client is created with a 4096 bit RSA key pair.
    The key pair is then hashed with sha256. The hex output from that
    gives you the 'client_id'
    """

    def __init__(self):
        self._private_key = RSA.generate(4096, new().read)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def client_id(self):
        return SHA256.new(self._public_key.exportKey('DER')).hexdigest()

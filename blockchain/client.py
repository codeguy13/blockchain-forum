from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Random import new


class Client:
    """!
    Client is created with a 4096 bit RSA key pair.
    The public key is exported then hashed with sha256.
    The hex output from that gives you the 'client_id'
    """

    def __init__(self):
        self.__private_key = RSA.generate(4096, new().read)
        self.public_key = self.__private_key.publickey()
        self.signer = PKCS1_v1_5.new(self.__private_key)
        self.communicator = PKCS1_OAEP.new(self.__private_key)

    @property
    def client_id(self):
        return SHA256.new(self.public_key.exportKey('DER')).hexdigest()

import time
import collections
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


class Transaction:
    def __init__(self, tx_amount, sender, reciever):
        self.tx_timestamp = time.time()
        self.tx_amount = tx_amount
        self.sender = sender
        self.reciever = reciever

    def get_tx_dict(self):
        if self.sender == "genesis_block":
            client_id = "genesis_block"
        else:
            client_id = self.sender.client_id

        return collections.OrderedDict(
            {
                "sender": client_id,
                "reciever": self.reciever,
                "amount": self.tx_amount,
                'timestamp': self.tx_timestamp
            }
        )

    def sign_tx(self):
        priv_key = self.sender._private_key
        signer = PKCS1_v1_5.new(priv_key)
        d = SHA256.new(str(self.get_tx_dict()).encode('utf8'))
        return signer.sign(d).hex().encode("ascii")

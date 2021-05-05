import time
import collections
from Crypto.Hash import SHA256


class Transaction:
    """Create a transaction instance to add to the blockchain"""

    def __init__(self, tx_data, sender, receiver):
        self.tx_timestamp = time.time()
        self.tx_data = tx_data
        self.sender = sender
        self.receiver = receiver
        self.sig = [self.tx_timestamp]

    def get_tx_dict(self):
        """
        Create transaction dictionary
        to put into transactions list on the block
        """

        return collections.OrderedDict(
            {
                "sender": self.sender.client_id,
                "receiver": self.receiver.client_id,
                "data": self.tx_data,
                "timestamp": self.tx_timestamp,
                "sig": self.sig
            }
        )

    @property
    def tx_signature(self):
        """Sign the transaction with senders private key"""

        tx_hash = SHA256.new(str(self.get_tx_dict()).encode())
        sig = self.sender.signer.sign(tx_hash)
        return self.sig.append(sig)

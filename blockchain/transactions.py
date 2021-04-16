import time
import json
from blockchain.blockchain import Block


class Transaction:
    def __init__(self, tx_index, tx_timestamp, tx_amount, sender, reciever):
        self.tx_index = tx_index
        self.tx_timestamp = tx_timestamp
        self.tx_amount = tx_amount
        self.sender = sender
        self.reciever = reciever
    
    
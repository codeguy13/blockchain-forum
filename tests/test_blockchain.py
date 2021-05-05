from blockchain.blockchain import Blockchain
from blockchain.client import Client
from blockchain.transactions import Transaction


def test_genesis_block():
    bc = Blockchain()
    assert bc.chain[0]


def test_add_block():
    bc = Blockchain()
    client1 = Client()
    client2 = Client()
    tx = Transaction(
        "Hello from the beginning",
        client1,
        client2
    )
    bc.unconfirmed_transactions.append(tx.get_tx_dict())
    bc.mine(bc.chain[-1])
    assert bc.chain[-1].transactions is not None

from blockchain.transactions import Transaction
from blockchain.client import Client


def test_transaction():
    client1 = Client()
    client2 = Client()
    tx = Transaction(
        client1,
        client2,
        "Test data"
    )
    assert tx.sig is not None

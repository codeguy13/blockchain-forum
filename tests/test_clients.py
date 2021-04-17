from blockchain.client import Client


def test_clients():
    client = Client()
    assert client.client_id.isascii

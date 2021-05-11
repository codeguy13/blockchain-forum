from blockchain.client import Client
from blockchain.interface.client_ui import ClientUI
import os


def test_clients():
    client = Client()
    assert client.client_id.isascii


def test_new_client_ui():
    client = ClientUI()
    client.output_client_info()
    with open('private_key.pem', 'r') as f:
        assert f.read()
        f.close()

    assert client.output_client_info() is not None

    if os.path.exists("private_key.pem"):
        os.remove("private_key.pem")
    else:
        print('File not found')

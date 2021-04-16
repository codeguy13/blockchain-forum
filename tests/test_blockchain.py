from blockchain.blockchain import Blockchain


def test_genesis_block():
    bc = Blockchain()
    bc.create_genesis_block()
    assert bc.chain[0]

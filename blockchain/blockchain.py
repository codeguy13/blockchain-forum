from Crypto.Hash import SHA256
import time


class Block:
    """!
    Blocks are where 'transactions' are stored.
    'Transactions' can be anything at the moment
    Block data will be hashed and fed into next block
    """
    # TODO: Add max block size
    # TODO: Add block headers for indexing and proof of work

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.target = 3

    def hash_block(self):
        """!
        Runs block data through SHA256 and returns the digest
        """

        block_string = str(self.__dict__)
        return SHA256.new(block_string.encode()).hexdigest()


class Blockchain:
    """!
    This will act as the database for the forum
    """
    # TODO: 'target' could use some work probably
    # TODO: Implement consensus using p2p
    # TODO: Encrypt data where needed
    # TODO: CONFIRMATIONS!!!

    DIFFICULTY = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """!
        The genesis block is the first block in the blockchain
        """
        # TODO: create hilarious genesis block data

        genesis_block = Block(0, ["WHAT THE HELL IS THIS!"], time.time(), "0")
        genesis_block.hash = genesis_block.hash_block()
        self.chain.append(genesis_block)

    def add_block(self, block, proof):
        previous_hash = self.previous_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    @property
    def previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        block.nonce = 0
        generated_hash = block.hash_block()
        while not generated_hash.startswith('0' * (Blockchain.DIFFICULTY + block.target)):
            block.nonce += 1
            generated_hash = block.hash_block()
            print(block.nonce, generated_hash)
        return generated_hash

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * (Blockchain.DIFFICULTY + block.target))
                and (block_hash == block.hash_block()))

    def mine(self, block):
        if not self.unconfirmed_transactions:
            return False
        previous_block = self.previous_block

        new_block = Block(
            index=previous_block.index + 1,
            transactions=self.unconfirmed_transactions,
            timestamp=time.time(),
            previous_hash=self.previous_block.hash
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

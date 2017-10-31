"""
Python implementation of a blockchain.

Writing a blockchain for the sake of learning about it
and also joining in on the hype
"""
import hashlib
from time import time
from uuid import uuid4


class Block(object):
    """Base block of a blockchain."""

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.new_block(previous_hash=1, proof=100) # genesis block

    def create_new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.transactions = []

        self.chain.append(block)
        return block

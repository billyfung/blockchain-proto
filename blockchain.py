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

    def __init__(self, index, block_hash, prev_hash, timestamp, proof):
        self.index = index
        self.hash = block_hash
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.proof = proof

    def create_new_block(cls, proof, prev_block=None):
        if prev_block:
            index = prev_block.index + 1
            prev_hash = prev_block.hash
        else:
            index = 0
            previous_hash = None

        block_hash = calculate_hash(
            index=index,
            timestamp=time(),
            proof=proof,
            prev_hash=prev_hash
        )

        block = {
            'index': index,
            'timestamp': time(),
            'proof': proof,
            'block_hash': block_hash,
            'prev_hash': prev_hash
        }

        return block

    def calculate_hash(index, timestamp, proof, prev_hash):
        """
        Creates a SHA-256 hash of a Block
        """

        str_to_hash = str(index) + str(timestamp) + str(proof) + str(prev_hash)
        block_hash = hashlib.sha256()
        block_hash.update(str_to_hash.encode())
        return block_hash


    # def build_genesis_block()
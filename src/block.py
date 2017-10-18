from datetime import datetime
from random import randint
from sys import maxint
from constants import MINING_HARDNESS, MINING_CHARACTER

class Block():
    def __init__(self, index, transactions, prev_hash, message):
        self.index = index
        self.date = datetime.now()
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.message = message
        self.hash = self.proof_of_work()

    def proof_of_work(self):
        block_hash, content = "", str(self.index) + str(self.prev_hash)
        while block_hash[:MINING_HARDNESS] != MINING_CHARACTER *\
                                              MINING_HARDNESS:
            magic_number = str(randint(0, maxint))
            block_hash = str(hash(content + magic_number))[1:]

        return block_hash

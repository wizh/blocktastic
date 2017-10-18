from datetime import datetime
class Block():
    def __init__(self, index, transactions, prev_hash, message):
        self.index = index
        self.date = datetime.now()
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.message = message
        self.hash = self.proof_of_work()

    def proof_of_work(self):
        pass

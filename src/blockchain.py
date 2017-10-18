from constants import GENESIS_INDEX, GENESIS_MESSAGE
import block

class Blockchain():
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    def get_latest_block(self):
        return self.blocks[-1]

    def get_block(self, index):
        if index < 0 or index >= len(self.blocks):
            raise ValueError("Block with index does not exist")

        return self.blocks[index]

    def create_genesis_block(self):
        if len(self.blocks) != 0:
            raise ValueError("Blockchain is not empty")

        genesis_block = block.Block(GENESIS_INDEX, [], "", GENESIS_MESSAGE)
        self.add_block(genesis_block)

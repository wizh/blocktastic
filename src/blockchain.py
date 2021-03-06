from constants import GENESIS_INDEX, GENESIS_MESSAGE
import block

class Blockchain():
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        if len(self.blocks) == 0:
            raise ValueError("No genesis block")
        if block.index != self.blocks[-1].index + 1:
            raise ValueError("Block index invalid")

        self.blocks.append(block)

    def get_latest_block(self):
        if len(self.blocks) == 0:
            raise ValueError("No genesis block")

        return self.blocks[-1]

    def get_block(self, index):
        if index < 0 or index >= len(self.blocks):
            raise ValueError("Block with index does not exist")

        return self.blocks[index]

    def create_genesis_block(self):
        if len(self.blocks) != 0:
            raise ValueError("Blockchain is not empty")

        genesis_block = block.Block(GENESIS_INDEX, [], "", GENESIS_MESSAGE)
        self.blocks = [genesis_block]

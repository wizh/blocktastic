# blocktastic
blocktastic is a reference blockchain implementation with no exotic features. It serves as a generic starting point for blockchain applications.

## Usage
One can create a blockchain
```python
from blockchain import Blockchain

blockchain = Blockchain()
blockchain.create_genesis_block()
```
A client could then append 10 blocks to said blockchain
```python
from block import Block

for i in range(10):
    prev_block = blockchain.get_latest_block()
    new_block = Block(prev_block.index + 1, [],
                      prev_block.hash, "I found block number " + str(i+1))
    blockchain.add_block(new_block)
```

## Todo
+ Add a peer-to-peer interface

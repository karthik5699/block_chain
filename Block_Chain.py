import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Block chain technology should have a block where each block has a unique number, time when
        it is created, the actual data or string, the hash value of previous block.
        All this contributes to the working of block-chain

        :param index: index is the unique number to each block
        :param timestamp: the time the block is created
        :param data: the value or the string
        :param previous_hash: the hash value of previous block

        The block chain working is pretty much same as the linked-lists where the each element has its own value and
        a link to its previous value, which forms a chain.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        """

        :return: it returns the hashed value based on sha256. It determines the sha value based on index time data previous hash
        all combined.
        """
        sha = hasher.sha256()
        line = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)
        sha.update(line.encode('utf-8'))
        return sha.hexdigest()



# Implementation of block-chain

def create_genesis_block():
    """
    Create_genesis_block is used to create the first block in the block-chain, it is the default
    function name for creating the first block in block-chain
    :return:
    """
    return Block(0, date.datetime.now(), 'Genisis Block', '0')

def next_block(last_block):
    """

    :param last_block: the next block in block chain is created using the hash value of previous block so
    it is used as parameter
    :return: it returns a new block with index being increased by 1, time to present time and new data each time.
    """
    new_index = last_block.index + 1
    new_timestamp = date.datetime.now()
    new_data = 'Hey i am ' + str(new_index)
    new_hash = last_block.hash
    return Block(new_index, new_timestamp, new_data, new_hash)

def block_connector():
    """
    The function to implement the block chain. The blockchain variable is assigned to the first value
    in the block chain using create_genesis_block
    :return:
    """

    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    number = 10
    for i in range(number):
        #assign block_to_add to next_block() using previous_block
        block_to_add = next_block(previous_block)

        #append to blockchain array the new block
        blockchain.append(block_to_add)

        #assign previous_block to the new block created
        previous_block = block_to_add

        print('Hash value is ' + block_to_add.hash)
    # [print(b.previous_hash) for b in blockchain]


block_connector()




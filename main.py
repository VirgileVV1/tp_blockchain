from blockChain import BlockChain
from block import Block
from datetime import datetime

if __name__ == '__main__':
    print("Creation d'une blockchain permettant la gestion d'une cryptomonnaie")

    block_chain = BlockChain()
    block_chain.next_block("Block de test")
    print(block_chain)
    transaction1 = 'Virgile send 5 BTC to Fanny'
    print(transaction1)
    print(block_chain.is_valid_blockchain())
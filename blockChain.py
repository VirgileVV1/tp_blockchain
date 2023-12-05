# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:05:36 2023

"""

from block import Block 
import hashlib

class BlockChain:
    
    def __init__(self): 
        self.blocks = []
        self.blocks.append(Block(0, None, "Genesis Block"))
        
    def next_block(self, data):
        previous = self.blocks[-1]
        block = Block(previous.index + 1, previous.hash, data)
        if self.is_valid_block(block, previous):
            self.blocks.append(block)
        else: 
            print("Erreur, block invalide")
        
    def is_valid_block(self, block, previous_block) -> bool:
        if block.index != (previous_block.index + 1):
            print("Index du bloc invalide")
            return False
        
        if block.previous_hash != previous_block.hash:
            print("Hash précédent incorrect")
            return False
        
        block_hash = hashlib.sha256(
            ((str(block.index) 
                 + block.date 
                 + block.data 
                 + str(block.previous_hash)).encode())).hexdigest()
        if block.hash != block_hash:
            print("Hash invalide")
            return False
        
        return True
        
    def is_valid_genesis_block(self):
        genesis_block = self.blocks[0]
        
        if genesis_block.index != 0:
            print("Index du bloc invalide")
            return False
        
        if genesis_block.previous_hash != None:
            print("Hash précédent incorrect")
            return False
        
        block_hash = hashlib.sha256(
            ((str(genesis_block.index) 
                 + genesis_block.date 
                 + genesis_block.data 
                 + str(genesis_block.previous_hash)).encode())).hexdigest()
        if genesis_block.hash != block_hash:
            print("Hash invalide")
            return False
        
        return True
    
    def is_valid_blockchain(self):
        if not self.is_valid_genesis_block():
            print("Erreur, genesis block invalide")
            return False
        
        for i in range(1, len(self.blocks)):
            if not self.is_valid_block(self.blocks[i], self.blocks[i-1]):
                return False
            
        return True
    
    def __str__(self):
        block_chain = ""
        for i in range(0, len(self.blocks)):
            block_chain = block_chain + str(self.blocks[i]) + "\n"
                            
        return block_chain
        
        
        
block_chain = BlockChain()
block_chain.next_block("Block de test")
print(block_chain)

print(block_chain.is_valid_blockchain())


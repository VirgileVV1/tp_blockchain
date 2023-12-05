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
        
        
block_chain = BlockChain()
block_chain.next_block("Block de test")
print(block_chain.blocks[-1])
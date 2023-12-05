# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:28:06 2023

"""

import hashlib

class Block:
    
    def __init__(self, previous_block, transaction_list):
        self.previous_block = previous_block
        self.transaction_list = transaction_list
        
        self.data = 
        self.hash = hashlib.sha256(self.data).hexdigest()
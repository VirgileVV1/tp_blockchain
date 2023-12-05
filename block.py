# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:28:06 2023

"""

import hashlib

from datetime import datetime

class Block:
    
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.date = datetime.now().strftime("%A %d %B %Y a %H:%M:%S")
        self.data = data
        self.hash = self.calculate_hash()
           
    def __str__(self):
        return f"Block {self.index} créé le {self.date} contenant : {self.data}"                     
    
    def calculate_hash(self):
        return hashlib.sha256(
            ((str(self.index) 
                 + self.date 
                 + self.data 
                 + str(self.previous_hash)).encode())).hexdigest()
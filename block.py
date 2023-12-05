# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:28:06 2023

"""
import re
import hashlib

from datetime import datetime

class Block:
    
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.date = datetime.now().strftime("%A %d %B %Y a %H:%M:%S")
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()
           
    def __str__(self):
        return f"Block {self.index} créé le {self.date} contenant : {self.data}"                     

    def is_data_correct(self) -> bool:
        #regex = re.compile("^[A-Z][a-z]*[-]?[A-Z][a-z]* send")

        regex = re.compile("^[A-Z][a-z]{1,20}[-]?([A-Z][a-z]{1,20})?\s(sends)\s([0-9].[0-9])\s(BC)\s(to)\s[A-Z][a-z]{1,20}[-]?([A-Z][a-z]{1,20})?$")
        
        print(regex.match(self.data))
        print(regex.match(self.data) == True)
        
        if (regex.match(self.data)):
            return True
        return True

    def calculate_hash(self):
        return hashlib.sha256(
            ((str(self.index) 
                 + self.date 
                 + self.data 
                 + str(self.previous_hash)
                 + str(self.nonce)).encode())).hexdigest()
    
    def solve_proof_of_work(self, difficulty = 4):
        self.nonce = 0
        while True: 
            self.hash = self.calculate_hash()
            valid = self.hash[0 : difficulty]

            if valid == "".join(['0'] * (difficulty)):
                print("nonce : " + str(self.nonce) + " hash : " + self.hash)
                return True
            
            self.nonce += 1
#!/usr/bin/env python

import block
import hashlib

class userInterface:
    blockchain = []
    
    wallets = [100]*5
    currentTransactions = []

    # these four functions are required for the assignment
    def moneyTransfer(self):
        transaction = input("[from, to, amount]: ").split()
        try:
            transaction = [int(tx) for tx in transaction]
        except:
            print("ERROR: each argument should be an int")
            return
        try:
            assert len(transaction) == 3
        except:
            print("ERROR: there should be 3 arguments")
            return
        if (self.wallets[transaction[0]] < transaction[2]):
            print(f"ERROR: wallet {transaction[0]} has insufficient funds")
            return
        self.currentTransactions.append(transaction)

        self.wallets[transaction[0]] -= transaction[2]
        self.wallets[transaction[1]] += transaction[2]
        if (len(self.currentTransactions) == 2):            
            self.blockchain.append(self.mine())
            self.currentTransactions = []
        return

    def printBlockchain(self):
        for block in self.blockchain:
            print(block)
        return

    def printBalance(self):
        for i in range(5):
            print(f"{str(i)}: {str(self.wallets[i])}")
        return

    def printSet(self):
        print(self.currentTransactions)
        return

    def hash(self, block):
        concatenation = str(block.depth) + block.prev_hash + str(block.nonce) + str(block.tx)
        return hashlib.sha256(concatenation.encode()).hexdigest()

    def mine(self):
        newBlock = block.block()
        if (self.blockchain):
            newBlock.prev_hash = self.hash(self.blockchain[-1])
            newBlock.depth = self.blockchain[-1].depth + 1
        newBlock.tx = self.currentTransactions
        while(self.hash(newBlock)[:3] != "000"):
            newBlock.nonce += 1
        return newBlock

    def go(self):
        fns = {"1": self.moneyTransfer, "2": self.printBlockchain, "3": self.printBalance, "4": self.printSet}
        while(1):
            try: 
                com = input("Enter 1 (moneyTransfer), 2 (printBlockchain), 3 (printBalance) or 4 (printSet): ")
            except:
                print("Goodbye!")
                return
            try:
                fns[com]()
            except:
                if (com and (not com.isspace())):
                    print(com)
                    print("input should be 1, 2, 3 or 4")

def main():
    ui = userInterface()
    ui.go()

if __name__=="__main__":
    main()

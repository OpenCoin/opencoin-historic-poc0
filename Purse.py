#The purse

class Purse:

    def __init__(self,keys, banks):
        #init
        self.keys = keys
        self.banks = banks
        self.coins = []

    def values(self):
        #returns the values of all holded coins
        return []

    def coins(self):
        #returns all holded coins
        return []

    def requestMinting(self,value,bank=None):
        #requests a coin of a value from the specified bank
        #bank defaults to the first one available
        return 'minted Coin'

    def createCoin(self,value):
        #creates a coin, keeps it, return it as well
        return 'coin'

    def requestChange(self,oldcoins,newcoins,bank=None):
        #request the old coins being exchanged for new ones
        #would be good if old and new ones matched in sum of value
        return []

    def spent(self,value,otherpurse):
        #spent some money
        return true

    def receive(self,coins):
        #receive some money
        return 'value'




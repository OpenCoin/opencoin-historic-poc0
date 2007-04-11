#The purse

import Issuer
from Coin import Coin


class Wallet:

    def __init__(self,issuers):
        """
        Setup a wallet
        >>> url = 'http://localhost'
        >>> i = Issuer.Issuer(url,[1,2])
        >>> w = Wallet({url:i})

        Create coins
        >>> w.createCoins([1,1,2],url)

        The coins are only created,
        not signed yet
        >>> w.getBalance()
        {}


        >>> w.fetchSignedBlinds()
        >>> w.getBalance()
        {}
        >>> w.fetchSignedBlinds()
        >>> {url:4} == w.getBalance()
        True
        
        """
        #init
        self.issuers = issuers
        self.blanks = []
        self.coins = {}
        self.new = {}
        self.pending = {}
        self.valid = {}
        
    def values(self):
        #returns the values of all holded coins
        return []

    def coins(self):
        #returns all holded coins
        return []

    def createCoins(self,values,issuerurl=None):
        """requests a coin of a value from the specified issuer
        """
        issuer = self.issuers[issuerurl]    
        
        for v in values:
            #create blanks
            coin = Coin(issuer.url,issuer.getPubKeys()[v],v)
            blind = coin.getBlind()
            hash = coin.getHash()
            self.coins[hash] = coin
            self.pending[hash] = coin

        #self.fetchSignedBlinds()


    def fetchSignedBlinds(self):
        
        for hash,coin in self.pending.items():
            issuer = self.issuers[coin.issuerurl]
            
            status,message = issuer.getSignedBlind(coin.getBlind(),coin.value)
            if status == 200:
                coin.setSignature(message)
                self.valid[hash] = coin
                del(self.pending[hash])

            elif status in range(300,400):
                pass

            elif status >=400:
                #Mmm, the issuer did not like our attempt
                del(self.pending[hash])
                del(self.coins[hash])
                
    def getBalance(self):
        #out = dict([(i,0) for i in self.issuers.keys()])
        out = {}
        for coin in self.valid.values():
            out[coin.issuerurl] = out.setdefault(coin.issuerurl,0) + coin.value
        return out


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

def debug():
    url = 'http://localhost'
    i = Issuer.Issuer(url,[1,2])
    w = Wallet({url:i})
    print w.getBalance()
    w.createCoins([1,1,2],url)
    print w.getBalance()

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
        



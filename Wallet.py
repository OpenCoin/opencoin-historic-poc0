# (c) 2007 Nils Toedtmann, Joerg Baach, License GPL
#The purse

from Coin import Coin
from util import *

class Wallet:

    def __init__(self,issuers):
        """
        Setup a wallet
        >>> import Issuer
        >>> url = 'http://opencoin.net/cur1'
        >>> i = Issuer.Issuer(url,[1,2])
        >>> w = Wallet({url:i})

        Create coins
        >>> coin_values, rest = partition(i.mint.keys.keys(),20)
        >>> w.createCoins(coin_values,url)

        >>> w.createCoins(17,url)


        The coins are only created,
        not signed yet
        >>> w.getBalance()
        {}


        >>> w.fetchSignedBlinds()
        >>> w.getBalance()
        {}
        >>> w.fetchSignedBlinds()
        >>> {url:37} == w.getBalance()
        True
        

        Have another wallet
        >>> w2 = Wallet({url:i})
        >>> coin = w.valid.values()[0]

        #>>> `w.getBalance()`
        #>>> `w2.getBalance()`

        >>> w.sendCoins(w2,[coin])
        >>> coin.value == w2.getBalance()[url]
        True

        #>>> `w.getBalance()`
        #>>> `w.valid`
        #>>> `w2.getBalance()`


        Redeem a coin
        >>> w2.sendCoins(i,[coin],'my account: 123')
        money redeemed

        #>>> w2.sendCoins(i,[coin],'my account: 124')
        Traceback (most recent call last):
        ...
        DoubleSpending


        dict = {}: dict(a=2,b=3)
        list = []: [a,b,c]
        tuple = (): (a,b,c)

        """
        #init
        self.issuers = issuers
        self.blanks = []
        #TODO: replace dicts with lists/properties whatever
        self.coins = {}
        self.new = {}
        self.pending = {}
        self.valid = {}
        self.cointainers = ['coins','valid','pending','new']
        self.callbacks = {}

    def values(self):
        #returns the values of all holded coins
        return []

    def coins(self):
        #returns all holded coins
        return []

    def createCoins(self,values,issuerurl):
        """requests a coin of a value from the specified issuer
        """
        issuer = self.issuers[issuerurl]    
         
        if type(values) != type([]):
            values, rest = partition(issuer.getPubKeys().keys(),int(values))

        for v in values:
            #create blanks
            coin = Coin(issuer.getUrl(),decodeKey(issuer.getPubKeys_encoded()[str(v)]),v)
            blind = coin.getBlind()
            hash = coin.getHash()
            self.coins[hash] = coin
            self.pending[hash] = coin

        #self.fetchSignedBlinds()


    def fetchSignedBlinds(self):
        
        for hash,coin in self.pending.items():
            issuer = self.issuers[coin.issuerurl]
            #print  (str(coin.getBlind()).encode('base64'),coin.value)
            status,message = issuer.getSignedBlind(str(coin.getBlind()).encode('base64'),coin.value)
            if status == 200:
                coin.setSignature(long(message))
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


    def sendCoins(self,receiver,coins,message=None):
        coins_encoded = [encodeCoin(coin) for coin in coins] 
        result = receiver.receiveCoins(coins_encoded,message)
        if result:
            for coin in coins:
                self.deleteCoin(coin)


    def receiveCoins(self,coins,message=None):
        coins_decoded = [decodeCoin(coin) for coin in coins] 
        for callback in getCallbacks(self,'receiveCoins'):
            callback(self,coins,message)
        for coin in coins_decoded:
            #TODO make checks (double, allowedbanks)
            hash = coin.getHash()
            issuer = self.issuers[coin.issuerurl]
            issuer.checkDoubleSpending([coin.getHash()])
            if self.coins.has_key(hash):
                raise 'NilsWantsToSeeThisError'
            else:
                self.coins[hash] = coin
                self.valid[hash] = coin
                return True


    def deleteCoin(self,coin):
        for var in self.cointainers:
            d = getattr(self,var,{})
            hash = coin.getHash()
            if d.has_key(hash):
               del(d[hash])
        coin.deleted = True


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

from SimpleXMLRPCServer import SimpleXMLRPCServer
class WalletServer (Wallet):

    def __init__(self,issuers,ip="0.0.0.0",port="8000"):
        Wallet.__init__(self,issuers)
        server = SimpleXMLRPCServer((ip, port))
        server.register_function(self.receiveCoins)
        server.serve_forever()





def debug():
    url = 'http://localhost'
    i = Issuer.Issuer(url,[1,2])
    w = Wallet({url:i})
    print w.getBalance()
    w.createCoins([1,1,2],url)
    print w.getBalance()
    return w

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
        



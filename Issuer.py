import Mint
from util import *

class Issuer:
     
    def __init__(self,url,denominations,keysize=256):
        """Create an issuer"""
        self.keysize = keysize
        self.url = url
        self.mint = Mint.Mint(url,denominations,keysize)
        self.signed = {}
        self.pending = {}
        self.failed = {} #blind,reason
    
    def getUrl(self):
        return self.url

    def getPubKeys(self):
        """Return the public keys for signing coins
        >>> i = Issuer('http://localhost',[1,2])
        >>> len(i.getPubKeys()) == 2
        True
        """
        return self.mint.getPubKeys()


    def getPubKeys_encoded(self):
        return dict([(str(u),encodeKey(k)) for u,k in self.getPubKeys().items()])

    def triggerMinting(self):
        """
        fake async        
        """
        for blind,value in self.pending.items():
            #check for auth, but not quite yet ;-)
            if True:
                self.signed[blind] = self.mint.signBlind(blind,value)
            else:
                self.failed[blind] = (407,'Not authorized')

            del(self.pending[blind])



    def getSignedBlind(self,blind,value):
        
        blind = blind.decode('base64')
        if self.signed.has_key(blind):
            return (200,str(self.signed[blind]))
        
        elif self.failed.has_key(blind):
            return self.failed.pop(blind)

        elif self.pending.has_key(blind):
            self.triggerMinting()
            return (300, 'not finished')

        else:
            self.pending[blind]=value
            self.triggerMinting()
            return (301, 'blind accepted, not finished')




def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()        

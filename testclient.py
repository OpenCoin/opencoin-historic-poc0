import xmlrpclib
from Wallet import Wallet

url = 'http://localhost'

i =  xmlrpclib.ServerProxy('%s:8000' % url)
w = Wallet({url:i})

w.createCoins([1,1,2],url)
print w.getBalance()
w.fetchSignedBlinds()
print w.getBalance()
w.fetchSignedBlinds()
print w.getBalance()


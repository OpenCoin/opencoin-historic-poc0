import xmlrpclib
from Wallet import Wallet

url = 'http://localhost'
server = 'http://172.30.31.111'

i =  xmlrpclib.ServerProxy('%s:8000' % server)
w = Wallet({url:i})

w.createCoins([1,1,2],url)
print w.getBalance()
w.fetchSignedBlinds()
print w.getBalance()
w.fetchSignedBlinds()
print w.getBalance()


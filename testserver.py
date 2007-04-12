from SimpleXMLRPCServer import SimpleXMLRPCServer
server = SimpleXMLRPCServer(("0.0.0.0", 8000))
import Issuer
i = Issuer.Issuer('http://opencoin.net/cur1',[1,2])
server.register_function(i.getSignedBlind)
server.register_function(i.getPubKeys_encoded)
server.register_function(i.getUrl)
server.register_function(i.checkDoubleSpending)
server.register_function(i.receiveCoins)
server.serve_forever()




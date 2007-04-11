from SimpleXMLRPCServer import SimpleXMLRPCServer
server = SimpleXMLRPCServer(("localhost", 8000))
import Issuer
i = Issuer.Issuer('http://localhost',[1,2])
server.register_function(i.getSignedBlind)
server.register_function(i.getPubKeys_encoded)
server.register_function(i.getUrl)
server.serve_forever()




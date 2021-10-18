from xmlrpc.server import SimpleXMLRPCServer
import struct
from dataclasses import dataclass

    
def buscaSalario(nome):
    retorno='Nome não econtrado! Entre com um nome existente!'

    if(nome=='Pedro'):
        retorno='Operador' + "/" + '1200' 
    if (nome=='Sergio'):
        retorno='Programador' + "/" + '2220'
    return retorno
    

server = SimpleXMLRPCServer(("172.31.42.142",8081))
server.register_function(buscaSalario,"buscaSalario")

server.serve_forever()
    
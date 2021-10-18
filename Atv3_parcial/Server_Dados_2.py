import socket
import struct
from xmlrpc.server import SimpleXMLRPCServer
import struct
from dataclasses import dataclass


def buscaMaior(nome):
    
    retorno='Nada definido'

    if(nome=='Pedro'):
        retorno='Masculino' + '/' + str(20) 
    if (nome=='Lara'):
        retorno='Feminino' + '/' + str(19) 

    return retorno
    
server = SimpleXMLRPCServer(("172.31.42.142",8083))
server.register_function(buscaMaior,"buscaMaior")

server.serve_forever()    
import socket
import struct
from dataclasses import dataclass

HOST=    'localhost'
PORT=   8002

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Conecte um Server-cliente')
conn, ender = s.accept()

print('Conectado em', ender)

@dataclass
class Pessoa(object):
    nome: str
    nivel: str
    salbruto: float
    ndepend: int
    

p1= Pessoa('Pedro','A', 5000, 2)
p2= Pessoa('Lara','B', 6000, 0)



while True:
    nome = conn.recv(1024).decode()
    retorno='Nada definido'

    if(nome==p1.nome):
        retorno=p1.nivel + '\n' + str(p1.salbruto) + '\n'+ str(p1.ndepend) + '\n'
    if (nome==p2.nome):
        retorno=p2.nivel + '\n' + str(p2.salbruto) + '\n'+ str(p2.ndepend) + '\n'
    conn.send(retorno.encode('utf8'))
    
    
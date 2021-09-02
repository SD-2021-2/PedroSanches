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
    n1: float
    n2: float
    n3: float


p1= Pessoa('Pedro', 10, 7.5, 6)
p2= Pessoa('Lara', 9, 2, 7)



while True:
    nome = conn.recv(1024).decode()
    retorno='Nada definido'

    if(nome==p1.nome):
        retorno=str(p1.n2) + '\n' + str(p1.n2) + '\n' + str(p1.n3) + '\n'
    if (nome==p2.nome):
        retorno=str(p2.n2) + '\n' + str(p2.n2) + '\n' + str(p2.n3) + '\n'

    conn.send(retorno.encode('utf8'))
    
    
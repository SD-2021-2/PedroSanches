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
    altura: float
    sexo: str
    

p1= Pessoa('Pedro', 1.65, 'Masculino')
p2= Pessoa('Lara', 1.63, 'Feminino')



while True:
    nome = conn.recv(1024).decode()
    retorno='Nada definido'

    if(nome==p1.nome):
        retorno=str(p1.altura) + '\n' + p1.sexo + '\n'
    if (nome==p2.nome):
        retorno=str(p2.altura) + '\n' + p2.sexo + '\n'

    conn.send(retorno.encode('utf8'))
    
    
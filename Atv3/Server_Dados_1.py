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
    cargo: str
    salario: float
    

p1= Pessoa('Pedro','Operador', 1200)
p2= Pessoa('Sergio','Programador', 2220)



while True:
    nome = conn.recv(1024)
    retorno='Nada definido'

    if(nome.decode()==p1.nome):
        retorno=p1.cargo + '\n' + str(p1.salario) + '\n'
    if (nome.decode()==p2.nome):
        retorno=p2.cargo + '\n' + str(p2.salario) + '\n'

    conn.send(retorno.encode('utf8'))
    
    
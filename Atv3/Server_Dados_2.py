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
    sexo: str
    idade: int
    

p1= Pessoa('Pedro','Masculino', 20)
p2= Pessoa('Lara','Feminino', 19)



while True:
    nome = conn.recv(1024).decode()
    retorno='Nada definido'

    if(nome==p1.nome):
        retorno=p1.sexo + '\n' + str(p1.idade) + '\n'
    if (nome==p2.nome):
        retorno=p2.sexo + '\n' + str(p2.idade) + '\n'

    conn.send(retorno.encode('utf8'))
    
    
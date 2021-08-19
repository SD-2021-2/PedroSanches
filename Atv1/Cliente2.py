import socket

HOST=   '127.0.0.1'
PORT=   15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Nome: ')
nome = input()
s.sendall(str.encode(nome))

print('Sexo: masc = 1 e fem = 2 ')
sexo = input()
s.sendall(str(sexo).encode('utf8'))

print('Idade :')
idade = input()
s.sendall(str(idade).encode('utf8'))


maior = s.recv(1024)

print('Mensagem ecoada:', maior.decode())
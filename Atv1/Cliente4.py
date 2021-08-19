import socket

HOST=   '127.0.0.1'
PORT=   15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Sexo: 1 masc 2 fem  ')
sexo = input()
s.sendall(str(sexo).encode('utf8'))

print('peso:')
peso = input()
s.sendall(str(peso).encode('utf8'))

print('altura:')
altura = input()
s.sendall(str(altura).encode('utf8'))


ideal = s.recv(1024)

print('Mensagem ecoada:', ideal.decode())
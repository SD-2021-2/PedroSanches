import socket

HOST=   '127.0.0.1'
PORT=   15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('N1 : ')
n1 = input()
s.sendall(str(n1).encode('utf8'))

print('N2')
n2 = input()
s.sendall(str(n2).encode('utf8'))

print('N3')
n3 = input()
s.sendall(str(n3).encode('utf8'))


resultado = s.recv(1024)

print('Mensagem ecoada:', resultado.decode())
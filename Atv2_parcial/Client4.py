import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Altura: ")
n1 = input()
s.sendall((n1+'\n').encode())

print("Sexo: ")
n2 = input()
s.sendall((n2+'\n').encode())


resposta = s.recv(1024).decode()
print(resposta)


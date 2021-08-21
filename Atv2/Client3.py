import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite a N1: ")
n1 = input()
s.sendall((n1+'\n').encode())

print("Digite a N2: ")
n2 = input()
s.sendall((n2+'\n').encode())

print("Digite a N3: ")
n3 = input()
s.sendall((n3+'\n').encode())

resposta = s.recv(1024).decode()
print(resposta)


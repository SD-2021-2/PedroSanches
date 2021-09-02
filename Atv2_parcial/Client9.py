import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite o numero da carta (1 a 13): ")
cart = input()
s.sendall((cart+'\n').encode())

print("Digite o naipe (1 a 3): ")
naipe = input()
s.sendall((naipe+'\n').encode())


resposta = s.recv(1024).decode()
print(resposta)


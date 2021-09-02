import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite o nome: ")
nome = input()
s.sendall((nome+'\n').encode())

resposta = s.recv(1024).decode()
print(resposta)


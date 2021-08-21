import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite o Nome: ")
nome = input()
s.sendall((nome+'\n').encode())

print("Digite o Sexo: ")
sexo = input()
s.sendall((sexo+'\n').encode())

print("Digite a Idade: ")
idade = input()
s.sendall((idade+'\n').encode())

resposta = s.recv(1024).decode()
print(resposta)


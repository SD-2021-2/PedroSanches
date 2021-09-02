import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Nome: ")
n1 = input()
s.sendall((n1+'\n').encode())
print("Nivel: ")
n2 = input()
s.sendall((n2+'\n').encode())
print("Salario bruto: ")
n4 = input()
s.sendall((n4+'\n').encode())
print("Numero de dependentes: ")
n3 = input()
s.sendall((n3+'\n').encode())



resposta = s.recv(1024).decode()
print(resposta)


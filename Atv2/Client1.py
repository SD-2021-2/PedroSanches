import socket

HOST = 'LocalHost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite o Nome do Funcionario: ")
nome = input()
s.sendall((nome+'\n').encode())

print("Digite o Cargo do Funcionario: ")
cargo = input()
s.sendall((cargo+'\n').encode())

print("Digite o Salario do Funcionario: ")
salario = input()
s.sendall((salario+'\n').encode())

resposta = s.recv(1024)
print(resposta)


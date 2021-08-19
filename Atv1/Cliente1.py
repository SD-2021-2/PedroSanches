import socket

HOST=   '127.0.0.1'
PORT=   15000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Nome: ')
nome = input()
s.sendall(str.encode(nome))

print('Cargo : operador = 1 e programador = 2 ')
cargo = input()
s.sendall(str(cargo).encode('utf8'))

print('Salário :')
salario = input()
s.sendall(str(salario).encode('utf8'))


novoSalario = s.recv(1024)

print('Mensagem ecoada:', novoSalario.decode())
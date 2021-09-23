import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://172.31.44.18:8080/")

print('nome: ')
nome = input()

print('cargo : (operador ou programador)')
cargo = input()

print('Salário :')
salario = input()

resposta = s.calculaSalario(cargo,salario)

print(resposta)
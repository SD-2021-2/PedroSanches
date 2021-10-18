import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://172.31.44.18:8080/")

print("Digite o Nome do Funcionario: ")
nome = input()
resposta = s.calculaSalario(nome)
print(resposta)


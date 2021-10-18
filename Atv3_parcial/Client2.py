import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://172.31.44.18:8082/")

print("Digite o Nome da pessoa: ")
nome = input()

resposta = s.consultaMaior(nome)
print(resposta)


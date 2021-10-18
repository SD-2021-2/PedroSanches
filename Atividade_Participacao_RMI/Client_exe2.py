import Pyro4

#uri = input("Digite Pyro uri: ").strip()

nome = input("Digite seu nome: ").strip()
sexo = input("Digite seu sexo(masculino ou feminino): ").strip()
idade = input("Digite sua idade: ").strip()

#funcaoremote = Pyro4.Proxy(uri)
#print(funcaoremote.maior_idade(sexo,idade))

funcaoremote = Pyro4.Proxy("PYRONAME:funcaoremote")  
print(funcaoremote.maior_idade(sexo,idade))
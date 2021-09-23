import Pyro4

nome = input("Digite seu nome: ").strip()
sexo = input("Digite seu sexo(masculino ou feminino): ").strip()
idade = input("Digite sua idade: ").strip()
funcaoremote = Pyro4.Proxy("PYRONAME:funcaoremota")
print(funcaoremote.maior_idade(sexo,idade))
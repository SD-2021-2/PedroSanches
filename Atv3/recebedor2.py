import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:8000")

sub = "Maioridade"
subscriber.setsockopt(zmq.SUBSCRIBE, sub.encode())

while True:
    [file, nom, sex, idad] = subscriber.recv_multipart()

    nome = nom.decode()
    sexo = sex.decode()
    idade = int(idad.decode())

    if sexo == "Masculino" and idade >= 18 or sexo == "Feminino" and idade >= 21:
        resposta = "Atingiu a Maioridade!"
    else:
        resposta = "Nao atingiu a Maioridade!"

    print(nome+ " " +resposta)

subscriber.close()
context.term()
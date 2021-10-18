import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:8000")

sub = "Reajuste"
subscriber.setsockopt(zmq.SUBSCRIBE, sub.encode())
while True:
    [file, nom, car, sal] = subscriber.recv_multipart()

    nome = nom.decode()
    salario = float(sal.decode())
    cargo = car.decode()

    if cargo == "Operador":
        salario = salario*1.2
    elif cargo == "Programador":
        salario = salario*1.18

    print("Salario de " +nome+ " Reajustado para: " + str(salario))

subscriber.close()
context.term()
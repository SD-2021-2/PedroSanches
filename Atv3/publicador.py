import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:8000")
print("Publicador está funcionando!")

while True :
    publisher.send_multipart(["Reajuste".encode(), "Pedro".encode(), "Programador".encode(), "2000".encode()])
    publisher.send_multipart(["Maioridade".encode(), "Sergio".encode(), "Masculino".encode(), "35".encode()])
    publisher.send_multipart(["Reprovacao".encode(), "9.4".encode(), "8.1".encode(), "7.5".encode()])
    publisher.send_multipart(["CalcPeso".encode(), "1.65".encode(), "Feminino".encode()])
    publisher.send_multipart(["Categoria".encode(), "14".encode()])
    publisher.send_multipart(["SalarioLiquido".encode(), "Pedro".encode(),"C".encode(),"3000".encode(), "3".encode()])
    publisher.send_multipart(["Aposentado".encode(), "72".encode(), "38".encode()])
    publisher.send_multipart(["Credito".encode(), "450".encode()])

    time.sleep(1)

publisher.close()
context.term()
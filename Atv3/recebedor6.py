import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:8000")

sub = "SalarioLiquido"
subscriber.setsockopt(zmq.SUBSCRIBE, sub.encode())

while True:
    [file, nom, niv, salb, ndepend] = subscriber.recv_multipart()

    nome = nom.decode()
    nivel = niv.decode()
    salariobruto = float(salb.decode())
    numerodepend = int(ndepend.decode())

    if nivel == "A":
        if(numerodepend == 0):
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.97)
        else:
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.92)
    elif nivel == "B":
        if(numerodepend == 0):
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.95)
        else:
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.9)
    elif nivel == "C":
        if(numerodepend == 0):
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.92)
        else:
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.85)
    elif nivel == "D":
        if(numerodepend == 0):
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.9)
        else:
            resposta = nome+" de Nivel:"+nivel +" Salario Liquido:"+str(salariobruto*0.83)
    else:
        resposta = "Nivel invalido!"

    print(resposta)

subscriber.close()
context.term()
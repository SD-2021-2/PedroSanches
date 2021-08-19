import socket

HOST=    'localhost'
PORT=   15000

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Conecte um cliente')
conn, ender = s.accept()

print('Conectado em', ender)



while True:
    nome = conn.recv(1024)
    print(nome)

    cargo = int(conn.recv(32))
    print(cargo)    

    salario = int(conn.recv(1024))
    print(salario)

    if cargo == 1:
        novoSalario = salario * (120/100)
        
    elif cargo == 2:
        novoSalario = salario * (118/100)
        

    if not nome:
        print('Fechando a conexão')
        conn.close()
        break

    elif not cargo:
        print('Fechando a conexão')
        conn.close()
        break

    elif not salario:
        print('Fechando a conexão')
        conn.close()
        break
    
    conn.sendall(str(novoSalario).encode('utf8'))
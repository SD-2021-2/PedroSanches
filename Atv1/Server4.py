import socket

HOST=    'localhost'
PORT=   15000

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão de um cliente')
conn, ender = s.accept()

print('Conectado em', ender)



while True:
    sexo = int(conn.recv(1024))
    print(sexo)

    peso = int(conn.recv(1024))
    print(peso)    

    altura = int(conn.recv(1024))
    print(altura)

   
    if sexo==1:
        ideal=(72,7 * altura) - 58
    elif sexo==2:
        ideal=(62,1 * altura) - 44,7
   

    if not sexo:
        print('Fechando a conexão')
        conn.close()
        break

    elif not peso:
        print('Fechando a conexão')
        conn.close()
        break

    elif not altura:
        print('Fechando a conexão')
        conn.close()
        break
    
    conn.sendall(str.encode(ideal))

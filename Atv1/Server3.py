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
    n1 = int(conn.recv(1024))
    print(n1)

    n2 = int(conn.recv(1024))
    print(n2)    

    n3 = int(conn.recv(1024))
    print(n3)

    m=(n1+n2)/2

    m2=(m+n3)/2
   
    resultado = ' reprovado'

    if m >= 7:
        resultado = 'aprovado'      
    elif m>= 3 and m <= 7 :
        if m2 >= 5 :
            resultado = 'aprovado'
   

    if not n1:
        print('Fechando a conexão')
        conn.close()
        break

    elif not n2:
        print('Fechando a conexão')
        conn.close()
        break

    elif not n3:
        print('Fechando a conexão')
        conn.close()
        break
    
    conn.sendall(str.encode(resultado))
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

    sexo = int(conn.recv(32))
    print(sexo)    

    idade = int(conn.recv(1024))
    print(idade)

    maior = 'Menor de idade'

    if idade >= 18 :
        if sexo ==1:
            maior = 'Maior de idade'

        
    if idade >= 21 :
        if sexo == 2:    
            maior = 'Maior de idade'
    
    
        

    if not nome:
        print('Fechando a conexão')
        conn.close()
        break

    elif not sexo:
        print('Fechando a conexão')
        conn.close()
        break

    elif not idade:
        print('Fechando a conexão')
        conn.close()
        break
    
    conn.sendall(str(maior).encode('utf8'))
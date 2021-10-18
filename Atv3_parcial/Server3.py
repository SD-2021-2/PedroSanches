from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://172.31.42.142:8081/")

def calculaSalario(nome):     
    
    retorno=s.buscaSalario(nome)

    cargo,salario=retorno.split("/")
    
    if cargo == 'Operador':
        salario = int(salario) * (120/100)
        
    if cargo == 'Programador':
        salario = int(salario) * (118/100)      

    return ('Novo salario:'+str(salario))


server = SimpleXMLRPCServer(("172.31.44.18",8080))

server.register_function(calculaSalario,"calculaSalario")

server.serve_forever()
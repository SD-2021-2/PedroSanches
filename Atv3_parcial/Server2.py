from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://172.31.42.142:8083/")

def consultaMaior(nome):     
    
    retorno=s.buscaMaior(nome)

    sexo,idade=retorno.split("/")
    retorno = "Menor de idade"
    
    if sexo == 'Masculino':
        if(int(idade)>=18): retorno = "Maior de idade"
        
    if sexo == 'Feminino':
        if(int(idade)>=21): retorno = "Maior de idade"      

    return retorno


server = SimpleXMLRPCServer(("172.31.44.18",8082))

server.register_function(consultaMaior,"consultaMaior")

server.serve_forever()
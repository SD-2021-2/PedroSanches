from xmlrpc.server import SimpleXMLRPCServer

def calculaSalario(cargo,salario):     
    
    if cargo == 'operador':
        salario = float(salario) * (120/100)
        
    if cargo == 'programador':
        salario = float(salario) * (118/100)      

    print('Novo salario:', salario)

    return ('Novo salario:', salario)


server = SimpleXMLRPCServer(("172.31.44.18",8080))
server.register_function(calculaSalario,"calculaSalario")
server.serve_forever()
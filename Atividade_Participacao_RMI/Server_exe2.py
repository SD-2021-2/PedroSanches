import Pyro4

@Pyro4.expose
class funcaoremota(object):
    def maior_idade(self,sexo,idade):
        idadeint =  int(idade)
        if(sexo == "masculino"):
            if(idadeint>=18):
                return "Maior de idade"
            else:
                return "Menor de idade"
        else: 
            if(sexo == "feminino"):
                if(idadeint>=21):
                    return "Maior de idade"
                else:
                    return "Menor de idade"
            else:
                return "Informação inconstante"


daemon = Pyro4.Daemon()                
ns = Pyro4.locateNS()                  
uri = daemon.register(funcaoremota)   
ns.register("funcaoremota", uri)   

print("Ready.")
daemon.requestLoop() 
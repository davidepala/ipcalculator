import re
def inaddrcontrol(addroct):
    pattern = re.compile("^[1-9]$|^[1-9][0-9]$|^1[0-9][0-9]$|^2[0-4][0-9]$|^25[0-5]$")#definisco l'espressione regolare per validare l'ip
    ipaddrvalresult = pattern.match(addroct)#assegna a ipaddrvalresult il risultato dell'applicazione della regex definita in pattern alla variabile addroct
    ipaddrval=ipaddrvalresult.group()#isola il solo oggetto matchato
    return ipaddrval #ritorna la variabile definita nella riga precedente
    
    
ipaddr=[]#definisco la lista che conterrà gli ottetti in formato ascii
ipaddrdec=[]#definisco la lista che conterrà gli ottetti sotto forma di interi
ipaddr = input("inserisci un indirizzo ").split(".") #acquisice l'indirizzo e assegna alle variabili a1-4 le stringhe separate dai punti
indice=range(4) #genero iun range da 0 a 3
for i in indice:
    ottettovalidato=inaddrcontrol(ipaddr[i]) #assegno alla variabile ottettovalidato l'output della funzione inaddrcontrol   
    ipaddrdec.append(int(ottettovalidato)) #aggiungo la variabile ottettovalidado sotto dforma di intero alla lista ipaddrdec 
indirizzo = "l'indirizzo inserito è %d.%d.%d.%d "%(ipaddrdec[0],ipaddrdec[1],ipaddrdec[2],ipaddrdec[3])
print(indirizzo) 

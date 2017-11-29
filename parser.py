file=open("C:\L20171109.log", "r")
tekst=file.read()
file.close()
tekst=tekst.split("\n")
tekst.append("//DUPA//")
print (tekst)


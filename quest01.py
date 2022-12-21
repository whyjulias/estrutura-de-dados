nome = (input("digite o arquivo: "))
f = open (nome, 'r')
q = f.readlines()
print ("número de linhas:", len(q))

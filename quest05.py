arq = (input("digite o arquivo: "))
o = open( arq, 'r')
L = []
for i in o:
    L.append(i)
count = 0
for i in range (0, len(L)):
    

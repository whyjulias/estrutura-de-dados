arq = (input("digite o arquivo: "))
crctr = (input("insira a caractere: "))
o = open( arq, 'r')
L = []
for i in o:
    L.append(i)
count = 0
for i in range (0, len(L)):
    s = L[i]
    for j in s:
        if j == crctr:
           count = count +1
print ("essa caractere aparece" , count, "vezes")
    

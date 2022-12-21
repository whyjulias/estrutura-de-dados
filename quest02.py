arq = (input("digite o arquivo: "))
f = open (arq, 'r')
L = []
for i in f:
    L.append(i)
cont = 0
for i in range (0, len(L)):
    x = L[i]
    for j in x:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            cont = cont+1
print (cont)

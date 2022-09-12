#Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições. Imprima a 
#matriz no formato tradicional de linhas e colunas
m = []

for i in range(0, 5):
    m.append([])
    for j in range(0, 5):
        if i == j:
            m[i].append(1)
        else:
            m[i].append(0)
for k in range(0, 5):
    print(m[k])

#DIAGONAL principal e secundária
m = []
dS = []
dP = []
tam = int(input('Matriz quadrada de quanto: '))
for i in range (0, tam):
    m.append([])
    for j in range (0,tam):
        m[i].append(int(input("element:")))
        if i+j == tam-1:
            dS.append(m[i][j])
        if i == j:
            dP.append(m[i][j])

print(m)
print(dS)
print(dP)
#for line in m:
#    print (tuple(line))

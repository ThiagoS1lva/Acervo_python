m = []

for i in range (0, 2):
    linha = [0]*2
    m.append(linha)
    for j in range(0, 2):
        m[i][j] = int(input('Digite um numero: '))
print(m)

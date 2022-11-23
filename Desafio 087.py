m = []
somaP = somaC = maiorV = 0
for i in range(0, 3):
    m.append([])
    for j in range(0,3):
        m[i].append(int(input(f'Digite um número para {[i]}{[j]}: ')))
        if m[i][j]%2==0: # SE FOR PAR
            somaP += m[i][j]
        if j == 2: #SE ESTIVER NA TERCEIRA COLUNA
            somaC += m[i][j]
        if i == 1: #SE ESTIVER NA SEGUNDA LINHA
            if maiorV == 0:
                maiorV = m[i][j]
            elif m[i][j] > maiorV:
                maiorV = m[i][j]


for k in range(0, 3):
        print(m[k])

print(f'A soma dos pares é {somaP}, a soma da terceira coluna é {somaC}, e o maior valor da segunda linha é {maiorV}')
m = []
for i in range(0, 3):
    m.append([])
    for j in range(0,3):
        m[i].append(int(input(f'Digite um número para {[i]}{[j]}: ')))
for k in range(0, 3):
        print(m[k])

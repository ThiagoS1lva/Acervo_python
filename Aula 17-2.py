pessoas = []
dado = []
for i in range(0, 3):
    dado.append(input('Nome:'))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)
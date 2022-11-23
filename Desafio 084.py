# <= 70 LEVE
# >= 100 PESADO
pessoas = []
listaPessoas = []
leve = []
pes = []
maior = menor = 0

while True:
    pessoas.append(input('Digite seu nome: '))
    pessoas.append(int(input('Digite seu peso: ')))
    if len(listaPessoas) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    listaPessoas.append(pessoas[:])
    pessoas.clear()
    resp = input('Deseja continuar? (S ou N)')
    if resp in 'Nn':
        break
for i in range(0, len(listaPessoas)):
    if listaPessoas[i][1] <= 70:
        leve.append(listaPessoas[i][0])
    elif listaPessoas[i][1] >= 100:
        pes.append(listaPessoas[i][0])

print('-='*30)
print(f'Foram cadastradas {len(listaPessoas) }')
print(f'As pessoas mais leves são {leve}')
print(f'As pessoas mais pesadas são {pes}')
print(f'O menor peso é {menor}Kg e o maior é {maior}Kg')
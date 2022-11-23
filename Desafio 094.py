dados = {}
pessoas = []
somaI = 0
mulheres = []
while True:
    dados['nome'] = input('nome: ')
    dados['sexo'] = input('sexo (M ou F): ')
    dados['idade'] = int(input('idade: '))
    somaI += dados['idade']
    if dados['sexo'] in 'Ff':
        mulheres.append(dados.copy())
    pessoas.append(dados.copy())
    resp = input('Quer continuar? ')
    if resp in 'nN':
        break

mediaI = somaI / len(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A media de idades é de {mediaI:.2f} Anos')
print(f'Lista com só as mulheres ', end='')
for k in range(0, len(mulheres)):
    print(mulheres[k]['nome'], end='')
print(f'Pessoas com idade acima da media: ', end='')
for j in range(0, len(pessoas)):
    if pessoas[j]['idade'] > mediaI:
        print(pessoas[j]['nome'], end='')

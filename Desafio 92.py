pessoa = {}

pessoa['Nome'] = input('nome: ')
pessoa['Ano de nasc'] = int(input('ano de nascimento: '))
pessoa['Carteira'] = int(input('Carteira de trabalho( < 0 não tem): '))
pessoa['Idade'] = 2022 - pessoa['Ano de nasc']
if pessoa['Carteira'] >= 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['aposentar'] =(pessoa['Ano de contratação'] + 35) - pessoa['Ano de nasc']

for k, v in pessoa.items():
    print(f'{k} = {v}')

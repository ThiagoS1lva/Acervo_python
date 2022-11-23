aluno = {}
aluno['nome'] = input('Nome: ')
aluno['Media'] = float(input('Media: '))

if aluno['Media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'Nome  = {aluno["nome"]}\nMedia = {aluno["Media"]}\nSituação = {aluno["situação "]}')

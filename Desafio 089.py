medias = []
alunos = []
notas = []

while True:
    alunos.append(input('Digite o nome do aluno: '))
    notas.append(float(input('Digite a nota 1 do aluno: ')))
    notas.append(float(input('Digite a nota 2 do aluno: ')))
    alunos.append(notas[:])
    medias.append(alunos[:])
    alunos.clear()
    notas.clear()
    resp = input('s ou n:')
    if resp in 'nN':
        break
for i in range(0, len(medias)):
    print(f'No Nome                     MEDIA')
    print(f'{i}  {medias[i][0]}                        {(medias[i][1][0]+medias[i][1][1])/2}')
busca = 0
while busca != 999:
    busca = int(input('Mostrar as notas de qual aluno? (999 para interromper): '))
    print(f'A nota de {medias[busca][0]} são {medias[busca][1]}')
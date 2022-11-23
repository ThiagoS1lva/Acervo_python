jogador = {}
jogador['nome'] = input('nome: ')
totP = int(input('Quantidade de partidas: '))
somaG = 0
gols = []


for i in range(0, totP):
    gol = int(input(f'Quantos gols na partida {i+1}: '))
    somaG += gol
    gols.append(gol)
jogador['gols'] = gols
jogador['gols no campeonato'] = somaG

for k, v in jogador.items():
    print(f'{k} = {v}')
for i in range(0, len(gols)):
    print(f'Na partida {i+1}, fez {gols[i]} ')
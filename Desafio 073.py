time = ('Palmeiras', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Goias',
                                                                                                'Santos', 'Bragantino')
print(f'Os 5 primeiros colocados são {time[:5]}')
print(f'Os 4 ultimos colocados da tabela são {time[-4:]}')
print(f'A lista de times em ordem alfabetica é {sorted(time)}')
print(f'O Internacional está na {time.index("Internacional")+1}º posição')
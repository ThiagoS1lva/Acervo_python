estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy()) #.copy para copiar

for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
    
#pessoas = {'nome' : 'Thiago', 'sexo' : 'M', 'Idade' : 20}
#del pessoas['sexo']
#pessoas['nome'] = 'Julia' #MODIFICIANDO
#pessoas['peso'] = 61.2 #ADICIONANDO

#for k,v in pessoas.items():
#    print(f'{k} = {v}')

estado = {'uf' : 'Rio de janeiro', 'sigla' : 'RJ'}
estado1 = {'uf' : 'São Paulo', 'sigla' : 'SP'}
estado2 = {'uf' : 'Minas Gerais', 'sigla' : 'MG'}
brasil = []
brasil.append(estado)
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1])
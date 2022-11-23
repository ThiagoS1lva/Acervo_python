#dicionário = {} #Identificados por chaves
#dados = dict()
#dados = {'nome': 'Pedro',
#         'idade': 25}
#print(dados)
#para adicionar um elemento no dicionário é:
#dados['sexo'] = 'M' #dados = {'nome' : 'Pedro', 'idade' : 25, 'sexo' : 'M'}
#print(dados)
#para deletar:
#del dados['idade']
#print(dados)
#print(dados.values()) #Mostra os valores
#print(dados.keys()) #mostra as chaves
#print(dados.items()) #pega os valores e as chaves

filme = {'titulo' : 'StarWars', 'ano' : 1977, 'diretor' : 'George Lucas'}
filme1 = {'titulo' : 'Avengers', 'ano' : 2012, 'diretor' : 'Joss Whedon'}
filme2 = {'titulo' : 'Matrix', 'ano' : 1999, 'diretor' : 'Wachowski'}
locadora = []
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)
print(locadora[0]['titulo'])
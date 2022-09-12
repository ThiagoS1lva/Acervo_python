#Crie a função mat_transposta(matriz). A função deve receber uma matriz genérica 
#bidimensional, de qualquer tamanho (não necessariamente quadrada) e retornar a 
#matriz transposta, sem alterar a matriz original.
#--- FUNÇÃO DA MATRIZ TRANSPOSTA --- #
def transposta(matriz):
    mt = []
    for i in range(0, c):
        mt.append([])
        for j in range (0, l):
            mt[i].append(matriz[j][i])
    return mt

m = []
#--- DEFININDO TAMANHO DA MATRIZ --- #
while True:
    try:
        l = int(input('Quantas linhas: '))
        c = int(input('Quantas colunas: '))
    except ValueError:
        print('Digite apenas número!')
    else:
        break
#--- CRIANDO A MATRIZ E INSERINDO OS ELEMENTOS --- #
for i in range(0, l):
    m.append([])
    for j in range(0, c):
        while True:
            try:
                m[i].append(int(input('elemento: ')))
            except ValueError:
                print('Digite apenas numero!')
            else:
                break
print(m)
print(transposta(m))

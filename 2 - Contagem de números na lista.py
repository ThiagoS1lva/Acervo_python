#Leia um vetor de 40 posições e conte quantos elementos pares se encontram no 
#vetor
lista = []
contP = 0
for i in range(0, 10):
    while True:
        try:
            lista.append(int(input('Digite um valor: ')))
        except ValueError:
            print('Digite apenas números!')
        else:
            break
    if lista[i]%2 == 0:
        contP += 1
print(f'Foram encontrados {contP} numeros PARES')

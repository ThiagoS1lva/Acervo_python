lista = []
maiorP = []
maiorN = 0
menorP = []
menorN = 0

for i in range (0, 5):
    lista.append(int(input(f'Digite um número para a posição {i}: ')))
    if i == 0:
        maiorN = menorN = lista[i]
    elif lista[i] > maiorN:
        maiorN = lista[i]
    elif lista[i] < menorN:
        menorN = lista[i]

for j in range(0, len(lista)):
    if lista[j] == maiorN:
        maiorP.append(j)
    if lista[j] == menorN:
        menorP.append(j)
print('-'*10)
print(f'O menor número é {menorN} na posição {menorP} e o maior número é {maiorN} na posição {maiorP}')

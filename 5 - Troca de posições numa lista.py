# Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas 
#posições. Imprima o vetor original e o vetor trocado.

lista = []
a = []
b = []
for i in range (0, 8):
    lista.append(int(input('numero: ')))
for j in range (0, 4):
    a.append(lista[j])
    b.append(lista[j+4])
lista = b + a
print(lista)

lista = []
n = 0
for i in range(0, 5):
    try:
        n = int(input('Digite um valor: '))
    except(ValueError):
        print('por favor, digite um número!')
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for j in range(0, len(lista)):
            if n <= lista[j]:
                lista.insert(j,n)
                break

print(lista)
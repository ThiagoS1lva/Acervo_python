lista = []
parar = 's'
par = []
impar = []
cont = 0
while parar != 'n':
    lista.append(int(input('Digite um número: ')))
    if lista[cont]%2 == 0:
        par.append(lista[cont])
    else:
        impar.append(lista[cont])
    cont+=1
    parar = input('Deseja continuar? (s ou n): ')

print(lista)
print(f'A lista impar{impar}')
print(f'A lista par {par}')

lista = []
parar = 'n'

while parar != 's':
    lista.append(int(input('Digite um número: ')))
    parar = input('Deseja parar (s ou n): ')

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
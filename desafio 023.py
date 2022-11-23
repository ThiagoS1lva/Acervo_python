numero = int(input('Digite um número: '))

print(f'unidade: {numero // 1 % 10}')
print(f'dezena: {numero // 10 % 10}')
print(f'centena: {numero // 100 % 10}')
print(f'milhar: {numero // 1000 % 10}')

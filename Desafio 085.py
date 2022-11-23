num = [[], []]

for i in range(0, 7):
    n = int(input('Digite um número: '))
    if n%2 == 0: # É PAR
        num[0].append(n)
    else: # É IMPAR
        num[1].append(n)
num[0].sort()
num[1].sort()
print('-='*30)
print(f'A lista é {num}')
print(f'Os números pares são {num[0]}')
print(f'Os números impares são {num[1]}')
num = []
parar = 'n'
while parar != 's':
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
    else:
        print('Valor duplicado, não vou adicionar!')
    parar = input('Deseja parar? ')
print(f'A lista digitada em ordem crescente é {sorted(num)}')
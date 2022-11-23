import random
numero = random.randint(0, 5)
num = int(input('Digite um número: '))
if num == numero:
    print('Acertou!')
else:
    print(f'Errou! O número era {numero}')
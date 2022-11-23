n = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
num = -1
while num < 0 or num > 10:
    num = int(input('Digite um número de 0 até 10: '))
#for i in range(0, len(n)):
#    if num == i:
#        print(f'Você digitou o numero {n[i]}')
print(f'Você digitou o numero {n[num]}')
num = int(input('Digite um numero(1): '))
num2 = int(input('Digite um numero(2): '))
num3 = int(input('Digite um numero(3): '))

if num > num2+num3 or num2 > num3+num or num3>num+num2:
    print('Não é possivel formar um triangulo!')
else:
    print('é possivel formar um triangulo!')

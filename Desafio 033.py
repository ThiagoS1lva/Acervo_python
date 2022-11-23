num = int(input('Digite um numero(1): '))
num2 = int(input('Digite um numero(2): '))
num3 = int(input('Digite um numero(3): '))

if num > num2 and num > num3:
    print(f'{num} é o maior número!')
elif num2 > num and num2 > num3:
    print(f'{num2} é o maior numero!')
elif num3 > num and num3 > num2:
    print(f'{num3} é o maior número!')

if num < num2 and num < num3:
    print(f'{num} é o menor número!')
elif num2 < num and num2 < num3:
    print(f'{num2} é o menor numero!')
elif num3 < num and num3 < num2:
    print(f'{num3} é o menor número!')
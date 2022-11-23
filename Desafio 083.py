ex = input('Digite uma expressão: ')
a = f = 0
for i in ex:
    if i == '(':
        a += 1
    elif i == ')':
        f += 1
if a == f:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é valida')
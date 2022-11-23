def contador(inicio, fim, passo):
    for i in range(inicio, fim+1, passo):
        print(i, end=' ')
    if fim < inicio:
        for j in range(inicio, fim-1, -passo):
            print(j, end=' ')

print('CONTAGEM DE 1 ATÉ 10, PASSO 1')
contador(1, 10, 1)
print('')
print('CONTAGEM DE 10 ATÉ 0, PASSO 2')
contador(10, 0, 2)
print('')
print('AGORA É COM VOCÊ: ')
i = int(input('inicio:'))
f = int(input('fim: '))
p = int(input('passo: '))
contador(i, f, p)
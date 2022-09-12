#Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X, 
#imprimir quantas vezes o número X aparece no vetor.
num = []
cont = 0

for i in range (0, 10):
    while True:
        try:
            num.append(int(input('Digite um número: ')))
        except ValueError:
            print('Digite APENAS número!')
        else:
            break

busca = int(input('Digite um número a ser buscado: '))
for i in num:
    if busca == i:
        cont += 1
print(f'Foram encontrados {cont} numeros iguais ao digitado')

import random
import time
lista = []
jogos = []
cont1 = 0
qnt = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'---==| SORTEANDO {qnt} JOGOS|==---')
time.sleep(1)
while cont1 < qnt:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    time.sleep(0.5)
    print(f'Jogo {cont1+1}  {jogos[cont1]}')
    cont1 += 1



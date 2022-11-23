import random


def sorteia():
    lista = []
    for i in range(0, 5):
        lista.append(random.randint(0, 50))
    return lista


def somaPar(lista):
    somaP = 0
    for i in range(0, len(lista)):
        if lista[i]%2 == 0:
            somaP += lista[i]
    return somaP


a = sorteia()
print(a)
print(f'a soma dos valares pares é {somaPar(a)}')

def dobraLista(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i] * 2
    return lista


valores = []
for i in range(0, 4):
    valores.append(int(input('num: ')))

print(dobraLista(valores))
print(valores)
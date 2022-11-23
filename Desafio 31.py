dis = float(input('Digite a distancia da viagem em KM: '))
preco = 0
if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis* 0.45
print(f'Você deve pagar {preco:.2f}')
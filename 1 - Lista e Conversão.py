tempC = []
tempF = []
mediaC = media = somaC = somaF = 0
cont1 = cont2 = 0
for i in range(0, 50):
    while True:
        try:
            tempC.append(int(input('Digite a temperatura em C: ')))
        except ValueError:
            print('Digite apenas números!')
        else:
            break
    tempF.append(tempC[i]*1.8 + 32)
    somaC += tempC[i]
    somaF += tempF[i]

try:
    mediaC = somaC / len(tempC)
    mediaF = somaF / len(tempF)
except ZeroDivisionError:
    print('Não foi possivel dividir por zero')

print(f'A media das temperaturas em celsius é {mediaC}ºC')
print(f'A media das temperaturas em farenheit é {mediaF}ºF')
print('As temperaturas em celsius que ficaram acima da media foram:')
for j in range(0, len(tempC)):
    if tempC[j] > mediaC:
        print(tempC[j],'°C')
        cont1 += 1
print('\nAs temperaturas em farenheit que ficaram acima da media foram:')
for k in range(0, len(tempF)):
    if tempC[k] > mediaC:
        print(tempF[k],'°F')
        cont2 += 1
print(f'{cont1} temperaturas em Celsius ficaram acima da media')
print(f'{cont2} temperaturas em farenheit ficaram acima da media')

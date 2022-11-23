vel = float(input('Digite a velocidade do carro: '))
if vel > 80.0:
    print('Você foi MULTADO!')
    multa = (vel - 80) * 7
    print(f'Sua multa é de {multa:.2f} Reais')
else:
    print('Parabens, dirigindo com segurança!')
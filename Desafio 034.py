sal = float(input('Digite seu salário: '))
if sal > 1250.00:
    nSal += sal + (sal*0.10)
elif sal < 1250.00:
    nSal += sal + (sal*0.15)
print(f'Seu novo salário é de {nSal:.2f}')
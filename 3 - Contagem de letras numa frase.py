#3. Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto.
def contfrase(fras):
    contE = contV = contR = 0
    fras = fras.lower()
    for i in fras:
        if i in ' ':
            contE += 1
        if i in 'aeiou':
            contV += 1
    contR = len(fras) - contE - contV
    print(f'A frase tem {contV} vogais e {contE} espaços')
    print(f'Tirando as vogais e os espaços sobra {contR} letras')        
 
frase = input('Digite uma frase: ')
contfrase(frase)


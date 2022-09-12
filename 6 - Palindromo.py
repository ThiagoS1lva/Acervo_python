#Um palíndromo é uma cadeia que pode ser lida de frente para trás e de trás para 
#frente. Ex: ‘SOMOS’ ‘1234321’. Implemente a função palindromo(palavra). O 
#parâmetro palavra é uma string. A função deverá retornar True se for um palíndromo e 
#False caso contrário
def palindromo(palavra):
    result = 0
    tam =len(palavra) // 2
    for i in range(0, tam):
        if palavra[i] == palavra[len(palavra)-i-1]:
            result = True
        else:
            result = False
    return result


palavra = input('palavra: ')
print(palindromo(palavra))

nome = input('nome: ').strip()
print(f'Seu nome tem {nome.lower().count("a")} letras as, e ela aparece'
        f'na primeira vez na posição {nome.lower().find("a") + 1}')
print(f'A ultima vez que a letra A aparece é na {nome.lower().rfind("a")+1}')


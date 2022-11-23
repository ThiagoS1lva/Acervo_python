try:
    n = int(input('numero: '))
except ValueError:
    print('por favor, digite APENAS número!')
else:
    print(n)
finally:
    print('Volte sempre!')
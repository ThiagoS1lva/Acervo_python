import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Erro')
else:
    print('Tudo certo!')

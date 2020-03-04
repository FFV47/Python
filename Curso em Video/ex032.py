from termcolor import colored
from datetime import date

ano = int(input("Digite um ano qualquer, ou coloque 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é {colored('BISSEXTO', 'yellow')}")
else:
    print(f"O ano de {ano} {colored('NÃO', 'red')} é {colored('BISSEXTO', 'yellow')}")

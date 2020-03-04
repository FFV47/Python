from random import randint
from time import sleep
from termcolor import colored

num = randint(0, 5)

print(colored("-=-", "magenta") * 25)
print(colored("Vou pensar em um numero entre 0 e 5, tente adivinhar.", "yellow"))
print(colored("-=-", "magenta") * 25)

user = int(input(colored("Digite um numero para adivinhar se você acertou: ", "green")))
print(colored("PROCESSANDO...", "cyan"))
sleep(3)

if user == num:
    print(f"Você acertou!!! O numero sorteado foi {num}")
else:
    print(f"Você perdeu!!! O numero sorteado foi {num}")

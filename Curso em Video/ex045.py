from random import choice
from time import sleep

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Jogo do Pedra, Papel, Tesoura':^60} \033[m")
print("\033[34m=\033[m" * 60)

itens = ("Pedra", "Papel", "Tesoura")

comp = choice(itens)

user = str(input("Escolha Pedra, Papel ou Tesoura: "))

print("JO ", end="")
sleep(0.75)
print("KEN ", end="")
sleep(0.75)
print("PÔ!!!\n")
sleep(0.75)

print("=" * 60)
print(f"Computador escolheu \033[36m{comp}\033[m")
print(f"Você escolheu \033[34m{user}\033[m")
print("=" * 60)

if user == comp:
    print("\033[34mEMPATE\033[m")
elif (
    (user == "Pedra" and comp == "Papel")
    or (user == "Papel" and comp == "Tesoura")
    or (user == "Tesoura" and comp == "Pedra")
):
    print("\033[32mPC GANHOU\033[m")
elif (
    (user == "Pedra" and comp == "Tesoura")
    or (user == "Papel" and comp == "Pedra")
    or (user == "Tesoura" and comp == "Papel")
):
    print("\033[32mVOCÊ GANHOU\033[m")
else:
    print("\033[31mJODADA INVÁLIDA!!!\033[m")

from random import randint
from time import sleep

print(f"\033[32m {'Jogo Par ou Impar':^60} \033[m")
print("\033[34m+\033[m" * 60)
vitoria = 0

while True:
    escolha_pc = randint(0, 10)
    escolha_user = int(input("Digite um numero de 0 a 10: "))
    par_impar = " "
    while par_impar not in "IP":
        par_impar = str(input("Escolha par ou impar [I/P]: ")).strip().upper()[0]

    soma = escolha_pc + escolha_user
    print("-" * 60)
    print(f"Você jogou {escolha_user} e o PC jogou {escolha_pc}.", end=" ")
    if (soma % 2 == 0 and par_impar == "P") or (soma % 2 == 1 and par_impar == "I"):
        print(f"{soma} é PAR." if par_impar == "P" else f"{soma} é IMPAR.")
        print("-" * 60)
        vitoria += 1
        print("VOCE VENCEU!!!")
        print("Vamos jogar novamente...")
        sleep(2)
        print("-=" * 30)
    else:
        print(f"{soma} é IMPAR." if par_impar == "P" else f"{soma} é PAR.")
        print("-" * 60)
        print("VOCE PERDEU!!!")
        print("-=" * 30)
        print(f"Voce obteve {vitoria} vitória(s). GAME OVER!!!")
        break

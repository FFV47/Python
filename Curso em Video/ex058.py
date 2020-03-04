from random import randint

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Jogo da Adivinha':^60} \033[m")
print("\033[34m=\033[m" * 60)

num = randint(0, 10)

palpite = -1
cont = 0

while palpite != num:
    palpite = int(input("Tente adivinha o numero do computador: "))
    if palpite != num:
        if palpite > num:
            print("Menos...Tente novamente.")
        else:
            print("Mais...Tente novamente.")
        cont += 1
    else:
        cont += 1
        print(f"Voce acertou depois de {cont} tentativas, o PC pensou em {num}")

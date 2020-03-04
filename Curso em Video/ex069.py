print("\033[34m=\033[m" * 60)

mulher20 = homem = maior18 = 0

print(f"\033[1;32m {' Contagem de Pessoas ':=^60} \033[m")

while True:
    idade = int(input("Digite sua idade: "))
    sexo = opcao = " "

    while sexo not in "MF":
        sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]

    print("-" * 60)
    while opcao not in "SN":
        opcao = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    print("-" * 60)

    if idade >= 18:
        maior18 += 1

    if sexo in "M":
        homem += 1
    elif sexo in "F" and idade < 20:
        mulher20 += 1

    if opcao in "N":
        break

print(f"\033[1;31m{'-'}\033[m" * 60)
print(f"Pessoas maiores de idade: {maior18}")
print(f"Homens: {homem}")
print(f"Mulheres com menos de 20 anos: {mulher20}")

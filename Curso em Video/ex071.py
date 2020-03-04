print(f"\033[32m {'Caixa Eletrônico':^60} \033[m")
print("\033[34m+\033[m" * 60)

print(f"\033[1;32m{' BANCO DO BRASIL ':=^60}\033[m")
saque = int(input("Digite o valor do saque: R$ "))

while True:
    saque50 = saque // 50
    print(f"Cédulas de 50: {saque50}")
    if saque % 50 == 0:
        break
    saque -= saque50 * 50

    saque20 = saque // 20
    print(f"Cédulas de 20: {saque20}")
    if saque % 20 == 0:
        break
    saque -= saque20 * 20

    saque10 = saque // 10
    print(f"Cédulas de 10: {saque10}")
    if saque % 10 == 0:
        break
    saque -= saque10 * 10

    saque1 = saque
    print(f"Cédulas de 1: {saque1}")
    if saque1 != 1:
        break

print("=" * 60)
print("VOLTE SEMPRE!!!")

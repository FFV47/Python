from time import sleep

print("\033[34m+\033[m" * 60)
print("\033[32m Avaliação de Empréstimo \033[m")
print("\033[34m=\033[m" * 60)

casa = float(input("Digite o valor da casa: R$ "))
sal = float(input("Digite o seu salário: R$ "))
anos = int(input("Digite em quantos anos você deseja pagar: "))

prestacao = casa / (anos * 12)

print(
    f"\n\033[35mVoce deve pagar uma prestacão de R$ {prestacao:.2f} por {anos * 12:.2f} meses\n\033[m"
)
print(
    f"\033[34mPelo seu salário, sua prestacão fica limitada a R$ {0.3 * sal:.2f}\033[m"
)
print("\033[33mPROCESSANDO...\033[m")
sleep(2)

if prestacao <= sal * 0.3:
    print("\033[1;32mParabens! seu crédito foi aprovado para o empréstimo.\033[m")
else:
    print(
        f"\033[1;31mSinto Muito! A prestação de R$ {prestacao:.2f} excede o limite de R$ {0.3 * sal:.2f}\033[m"
    )

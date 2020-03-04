from datetime import date

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Contador de Maioridade':^60} \033[m")
print("\033[34m=\033[m" * 60)

maioridade = 0
menoridade = 0

for i in range(7):
    nascimento = int(input("Digite seu ano de nascimento: "))
    idade = date.today().year - nascimento
    print(idade)
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(
    f"Dentre as 7 pessoas: \n{maioridade} são maiores de idade \n{menoridade} são menores de idade"
)

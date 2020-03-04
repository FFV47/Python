from datetime import date

print("\033[34m+\033[m" * 60)
print("\033[32m Alistamento \033[m")
print("\033[34m=\033[m" * 60)

ano = int(input("Digite o ano do seu nascimento: "))

idade = date.today().year - ano

if idade < 18:
    print(f"Você tem {idade} anos")
    print(f"Faltam {18 - idade} anos para voce poder se alistar")
    print(f"Seu alistamento será em {ano + 18}.")
elif idade == 18:
    print(f"Voce ja tem {idade} anos, ja está na hora de se alistar")
else:
    print(f"Você tem {idade} anos")
    print(f"Você ja deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {ano + 18}.")

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Sexo em while':^60} \033[m")
print("\033[34m=\033[m" * 60)

sexo = "a"

while sexo not in "MmFf":
    sexo = str(input("Digite o sexo da pessoa: ")).strip()
    if sexo not in "MmFf":
        print("Dados Inválidos, digite novamente.")

if sexo in "Mm":
    print("Sexo Masculino registrado.")
else:
    print("Sexo Feminino registrado")

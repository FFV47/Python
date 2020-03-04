print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Nome, Idade e Sexo':^60} \033[m")
print("\033[34m=\033[m" * 60)

soma_idade = 0
velho = 0
menor_20 = 0

for i in range(4):
    print(f"\n\033[3{i+1}m{f' {i+1}ª Pessoa ':-^30}\033[m")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ")).strip()

    soma_idade += idade

    if sexo in "Mm" and idade > velho:
        velho = idade
        nome_velho = nome

    if sexo in "Ff" and idade <= 20:
        menor_20 += 1

print(f"\nMédia de idade do grupo: \033[36m{soma_idade / 4}\033[m anos")
print(
    f"\nO homem mais velho do grupo é \033[34m{nome_velho}\033[m, e ele tem \033[34m{velho}\033[m anos"
)
print(f"\nExistem \033[33m{menor_20}\033[m mulhere(s) com menos de 20 anos no grupo")

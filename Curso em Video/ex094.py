dados = dict()
cadastro = list()
total_idade = 0
mulher = list()

while True:
    dados["Nome"] = str(input("Nome: ")).strip()
    while True:
        dados["Sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
        if dados["Sexo"] in "MF":
            break
        print("ERRO!!! Sexo inválido. Tente novamente")

    dados["Idade"] = int(input("Idade: "))
    total_idade += dados["Idade"]
    if dados["Sexo"] in "Ff":
        mulher.append(dados["Nome"])
    cadastro.append(dados.copy())

    while True:
        resp = str(input("Deseja Continuar [S/N]? ")).upper().strip()[0]
        if resp in "SN":
            break
        print("Resposta inválida. Tente novamente")
    if resp in "Nn":
        break

media = total_idade / len(cadastro)
print("-" * 60)
print(f"Foram cadastradas {len(cadastro)} pessoas.")
print(f"A média de idade do grupo é {media:.2f}")
print(f"As mulheres no grupo são: {mulher}")
print(f"As pessoas que possuem idade acima da média são: ")
for p in cadastro:
    if p["Idade"] > media:
        print(" => ", end="")
        for k, v in p.items():
            print(f"{k} = {v}", end="   ")
        print()
print()

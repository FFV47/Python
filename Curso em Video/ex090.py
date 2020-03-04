aluno = list()
dados = dict()

while True:
    dados["nome"] = str(input("Nome: "))
    dados["media"] = float(input("Média: "))
    if dados["media"] < 5:
        dados["sit"] = "Reprovado"
    elif 7 > dados["media"] >= 5:
        dados["sit"] = "Recuperação"
    else:
        dados["sit"] = "Aprovado"
    aluno.append(dados.copy())
    dados.clear()

    n = str(input("Continuar [S/N]? "))
    if n in "Nn":
        break

print()
print(f"{' BOLETIM ':=^30}")
print(f"{'NOME':<10}{'MÉDIA':<5}{'SITUAÇÃO':>15}")
print("-" * 30)
for i in aluno:
    print(f"""{i['nome']:<10}{f"{i['media']:.1f}":<5}{i['sit']:>15}""")
print("-" * 30)
print()

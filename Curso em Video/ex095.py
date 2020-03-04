jog = dict()
dados = list()
maior = 0

while True:
    jog["Nome"] = str(input("Nome do Jogador: ")).strip()
    partidas = int(input(f"Quantas partidas {jog['Nome'].upper()} jogou? "))
    jog["Gols"] = list()
    jog["Total"] = 0
    for i in range(partidas):
        jog["Gols"].append(int(input(f"Quantos gols na partida {i}: ")))
        jog["Total"] += jog["Gols"][i]
    dados.append(jog.copy())

    while True:
        resp = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
        if resp in "SN":
            break
        print("Resposta inválida. Tente novamente")
    if resp in "Nn":
        break

print("=" * 45)
print(f"{'Código':<7}{'Nome':<13}{'Gols':<20}{'total':>5}")
print("-" * 45)
for i, v in enumerate(dados):
    print(f"{i:>6} {v['Nome']:<13}{str(v['Gols']):<20}{v['Total']:>5}")
print("=" * 45)

while True:
    num = int(input("Mostrar dados de qual jogador [999 para sair]: "))
    if num == 999:
        break
    elif num >= len(dados):
        print(f"ERRO! Não existe jogar com código {num}. Tente novamente.")
        print()
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR '{dados[num]['Nome']}':")
        for j, g in enumerate(dados[num]["Gols"]):
            print(f"   => No jogo {j}, fez {g} gol(s).")
        print()

print("<<< ENCERRADO >>>")
print()

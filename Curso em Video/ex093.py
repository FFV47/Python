jog = dict()

jog["Nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {jog['Nome']} jogou? "))
jog["Gols"] = list()
jog["Total"] = 0

for i in range(partidas):
    jog["Gols"].append(int(input(f"Quantos gols na partida {i}: ")))
    jog["Total"] += jog["Gols"][i]
print("-" * 60)
for k, v in jog.items():
    print(f"{k}: {v}")

print("-" * 60)
print(f"O jogador {jog['Nome']} jogou {partidas} partidas.")
for i, v in enumerate(jog["Gols"]):
    print(f"{f'=> Na partida {i}, fez {v} gol(s).':>34}")

print(f"Foi um total de {jog['Total']} gols.")
print()

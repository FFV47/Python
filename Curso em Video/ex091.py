from time import sleep
from random import randint
from operator import itemgetter

jogo = dict()
rankjog = list()
rankdado = list()

print("VALORES SORTEADOS:", end="\n\n")

for i in range(4):
    jogo[f"Jogador {i+1}"] = randint(1, 6)
    print(f"O Jogador {i+1} tirou {jogo[f'Jogador {i+1}']}")
    sleep(1)

print("\033[31m=\033[m" * 60)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(jogo)
print(ranking)
print("\033[31m=\033[m" * 60)
print("RANKING DOS JOGADORES:", end="\n\n")

for i, v in enumerate(ranking):
    print(f"{i+1}º Lugar, {v[0]} com {v[1]}")
    sleep(1)
print()

# Minha solução

# print("\033[31m=-\033[m" * 30)
# print("RANKING DOS JOGADORES:", end="\n\n")
# ordem = list(jogo.items())

# for i in range(len(ordem)):
#     nome = ordem[i][0]
#     valor = ordem[i][1]

#     if i == 0 or valor >= rankdado[-1]:
#         rankdado.append(valor)
#         rankjog.append(nome)
#     else:
#         for p, j in enumerate(rankdado):
#             if valor < j:
#                 rankdado.insert(p, valor)
#                 rankjog.insert(p, nome)
#                 break

# rankjog.reverse()
# rankdado.reverse()

# for i in range(len(jogo)):
#     print(f"{i+1}º Lugar, {rankjog[i]} com {rankdado[i]}")
#     sleep(1)
# print()

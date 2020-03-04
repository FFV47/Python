from random import sample
from time import sleep

jogos = []

print("-" * 60)
print(f"{'Jogos da Mega Sena':^60}")
print("-" * 60)

n = int(input("Digite quantos jogos você deseja: "))

print(f"{f' Sorteando {n} jogos ':=^60}")
for i in range(n):
    jogos.append(sample(range(1, 61), 6))
    print(f"Jogo {i+1}: \033[34m{jogos[i]}\033[m")
    sleep(1)

print(f"{' < BOA SORTE! > ':=^60}")

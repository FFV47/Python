from statistics import mean
from time import sleep

boletim = []
dados = []
notas = []

while True:
    dados.append(str(input("Digite o nome do aluno: ")))
    notas.append(float(input("Digite a 1ª nota: ")))
    notas.append(float(input("Digite a 2ª nota: ")))
    dados.append(notas.copy())
    boletim.append(dados.copy())
    notas.clear()
    dados.clear()
    n = str(input("Deseja continuar [S/N]? "))
    if n in "nN":
        break
print()
print(f"{'BOLETIM':=^20}")
print(f"{'No':<4}{'NOME':<11}{'Média':>5}")
print("-" * 20)
for p, i in enumerate(boletim):
    print(f"{p:<4}{i[0]:<11}{f'{mean(i[1]):.1f}':>5}")
print("-" * 20)

# Solução com nome
# while True:
#     n = str(input("Mostrar notas de qual aluno ? [Digite 'S' para sair]: "))
#     if n in "Ss":
#         break
#     for i in boletim:
#         if i[0] == n:
#             print(f"As notas de {i[0]} são '{i[1][0]}','{i[1][1]}'")
# print()

# Solução com indice
while True:
    n = str(input("Mostrar notas de qual aluno ? [Digite 'S' para sair]: "))
    if n in "Ss":
        break
    n = int(n)
    for p, i in enumerate(boletim):
        if p == n:
            print(f"As notas de {i[0]} são {i[1][0]} e {i[1][1]}")
    print("-" * 60)
print("FINALIZANDO....")
sleep(1)
print()

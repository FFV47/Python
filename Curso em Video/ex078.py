lista = []

for i in range(5):
    lista.append(int(input(f"Digite um valor para a {i}ª posição: ")))

print("-=" * 30)
print(f"Voce digitou os valores: \033[31m{lista}\033[m")
print("-=" * 30)

print(f"O Maior valor é \033[36m{max(lista)}\033[m, e esta nas posições: ", end="")

for p, i in enumerate(lista):
    if i == max(lista):
        print(f"\033[32m{p}\033[m", end=" ")

print("\n", "-" * 60)

print(f"O Menor valor é \033[36m{min(lista)}\033[m, e esta na posições: ", end="")

for p, i in enumerate(lista):
    if i == min(lista):
        print(f"\033[33m{p}\033[m", end=" ")

print("\n")

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Soma dos Multiplos de 3':^60} \033[m")
print("\033[34m=\033[m" * 60)

ini = int(input("Inicio: "))
fim = int(input("Fim: "))
soma = 0
soma_qtd = 0

for i in range(ini, fim + 1):
    if i % 3 == 0 and i % 2 == 1:
        print(i, end=" ")
        soma += i
        soma_qtd += 1
    if i % 100 == 0:
        print("\n")
print(f"A soma de todos os {soma_qtd} valores impares resulta em: {soma}")

# Segunda Solução Otimizada

soma = 0
soma_qtd = 0

print("\n")
for i in range(ini, fim + 1, 2):
    if i % 3 == 0:
        print(i, end=" ")
        soma += i
        soma_qtd += 1
    if i % 33 == 0:
        print("\n")

print(f"\nA soma de todos os {soma_qtd} valores impares resulta em: {soma}")

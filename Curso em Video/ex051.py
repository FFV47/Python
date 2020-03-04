print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Progressão Aritmética':^60} \033[m")
print("\033[34m=\033[m" * 60)

primeiro = int(input("Primeiro termo da PA: "))
razao = int(input("Razao da PA: "))

print(f"Progressão Aritmética com inicio em {primeiro} e razao {razao}:")
print("\nPrimeiros 10 termos da PA:", end=" ")

for i in range(primeiro, 10 * razao, razao):
    print(i, end=" -> ")
print("FIM")

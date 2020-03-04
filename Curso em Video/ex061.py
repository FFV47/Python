print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Progressão Aritmética em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

i = 1

print("10 primeiros termos da PA:", end=" ")
while i <= 10:
    print(f"{termo} ->" if i != 10 else f"{termo}", end=" ")
    termo += razao
    i += 1

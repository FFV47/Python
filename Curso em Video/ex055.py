print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Comparador de Peso':^60} \033[m")
print("\033[34m=\033[m" * 60)


peso = float(input("Digite seu peso: "))
maior = menor = peso

for i in range(4):
    peso = float(input("Digite seu peso: "))

    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print(f"Maior peso: \033[34m{maior}\033[m Kg")
print(f"Menor peso: \033[35m{menor}\033[m Kg")

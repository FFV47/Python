num = []

tam = int(input("Digite o tamalho da lista: "))
print("\033[31m=-\033[m" * 40)

for i in range(tam):
    n = int(input("Digite um valor: "))

    if i == 0 or n >= num[-1]:
        num.append(n)
        print("\033[32mAdicionado ao final da lista\033[m")
    else:
        for p, j in enumerate(num):
            if n < j:
                num.insert(p, n)
                print(f"\033[32mAdicionado {n} na posição {p}\033[m")
                break

print("\033[31m=-\033[m" * 40)
print(f"Os valores digitados em ordem: \033[34m{num}\033[m")

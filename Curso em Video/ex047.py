print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Numeros Pares no Intervalo':^60} \033[m")
print("\033[34m=\033[m" * 60)

ini = int(input("Inicio: "))
fim = int(input("Fim: "))

for i in range(ini, fim + 1):
    if i % 2 == 0:
        print(i, end=" ")
        if i % 10 == 0:
            print("\n")

# Segunda Solução

for i in range(2, 50 + 1, 2):
    print(i, end=" ")

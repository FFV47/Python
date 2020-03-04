from time import sleep

print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Contagem Regressiva':^60} \033[m")
print("\033[34m=\033[m" * 60)

cont = int(input("Estipule o tempo para a contagem regressiva: "))

for i in range(cont, 0, -1):
    print(i)
    sleep(1)

print("BOOM!!!")

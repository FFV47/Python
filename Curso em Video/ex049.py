print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Tabuada':^60} \033[m")
print("\033[34m=\033[m" * 60)

tab = int(input("Digite o numero pra qual deseja a Tabuada: "))

print(f"\nTabuada do numero {tab}:")
for i in range(1, 11):
    print(f"{i} x {tab} = {i * tab}")

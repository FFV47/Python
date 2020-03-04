print(f"\033[32m {'Tabuada em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

while True:
    num = int(input("Digite um numero para a tabuada: "))

    if num < 0:
        break

    print(f"\033[31m{'-'}\033[m" * 20)
    for i in range(1, 11):
        print(f"\033[32m{i} x {num} = {i * num}\033[m")
    print(f"\033[31m{'-'}\033[m" * 20)


print("FIM")

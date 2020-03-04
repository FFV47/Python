print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Fatorial em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

num = int(input("Digite um numero qualquer: "))

i = 1
fatorial = 1
print(f"{num}! =", end=" ")
while i <= num:
    fatorial *= i
    cont = num + 1 - i
    print(f"{cont}" if i == num else f"{cont} x", end=" ")
    i += 1
print(f"= \033[34m{fatorial}\033[32m")

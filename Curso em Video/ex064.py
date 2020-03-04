print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Soma em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

i = soma = num = 0

while num != 999:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    i += 1
    soma += num

print(f"Foram digitados \033[31m{i}\033[m e a soma entre eles é \033[34m{soma}\033[m")

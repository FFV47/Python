num = []
i = 0

while True:
    n = str(input('Digite um numero [Digite "S" para sair]: '))
    if n in "Ss":
        break
    n = int(n)
    num.append(n)
    i += 1

print("-=" * 30)
print(f"\033[32mForam registrados {i} valores na lista.\033[m")
num.sort(reverse=True)
print("-=" * 30)
print(f"A lista resgistrada é \033[31m{num}\033[m")
print("-=" * 30)
if 5 in num:
    print(f"O numero 5 foi digitado {num.count(5)} vezes")
else:
    print("O numero 5 não está na lista")

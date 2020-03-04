num = []

while True:
    n = str(input("\033[32mDigite um valor [Digite S para sair]:\033[m ")).upper()
    if n in "Ss":
        break
    n = int(n)
    if n in num:
        print(f"\033[34mO valor {n} ja foi digitado, tente novamente.\033[m")
    else:
        num.append(n)

# num.sort()
print("-=" * 30)
print(f"Os valores digitados foram: \033[35m{sorted(num)}\033[m")

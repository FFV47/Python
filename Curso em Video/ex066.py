print("\033[34m+\033[m" * 60)

soma = cont = 0

while True:
    num = int(input("Digite um numero (digite 999 para parar): "))
    if num == 999:
        break
    cont += 1
    soma += num

print(f"Foram digitados {cont} numeros e a soma é {soma}")

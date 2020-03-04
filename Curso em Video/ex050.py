print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Soma de Numeros Pares':^60} \033[m")
print("\033[34m=\033[m" * 60)

soma = 0
cont = 0
for i in range(6):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f"\nVocê digitou {cont} numero(s) pares e a soma é {soma}")

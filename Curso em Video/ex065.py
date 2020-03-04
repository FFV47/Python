print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Média em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

i = cont = soma = 0
opcao = "S"

while opcao in "S":
    num = int(input("Digite um um numero: "))
    opcao = str(input("Deseja continuar [S/N]: ")).strip().upper()

    if cont == 0:
        maior = menor = num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    cont += 1
    soma += num

print(f"Média: \033[32m{soma / cont:.2f}\033[m")
print(f"Maior: \033[33m{maior}\033[m")
print(f"Menor: \033[34m{menor}\033[m")
print(f"Total de numeros lidos: \033[35m{cont}\033[m")

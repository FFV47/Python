print("\033[34m+\033[m" * 60)
print("\033[32m Conversão de Base \033[m")
print("\033[34m=\033[m" * 60)

num = int(input("Digite um numero inteiro qualquer: "))

print("Escolha a base de conversão: \n1 -> Binário\n2 -> Octal\n3 -> Hexadecimal")
base = int(input("Digite a escolha de base de conversão: "))

if base == 1:
    print(f"O numero {num} na base binaria vale \033[32m{bin(num)[2:]}\033[m")
elif base == 2:
    print(f"O numero {num} na base octal vale \033[32m{oct(num)[2:]}\033[m")
elif base == 3:
    print(f"O numero {num} na base hexadecimal vale \033[32m{hex(num)[2:]}\033[m")
else:
    print("\033[31m" + "Não existe resposta para o numero digitado\033[m")

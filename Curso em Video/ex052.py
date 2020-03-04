print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Numero Primo':^60} \033[m")
print("\033[34m=\033[m" * 60)

num = int(input("Digite um numero qualquer: "))

i = 2
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"O numero {num} não é primo")
            break
    if i + 1 == num or num == 2:
        print(f"O numero {num} é primo")
else:
    print("O numero 1 não é primo")

# Segunda Solução

cont = 0
print(f"Divisores de {num}: ", end=" ")
for i in range(1, num + 1):
    if num % i == 0:
        print(f"\033[32m{i}\033[m", end=" ")
        cont += 1
    else:
        print(f"\033[31m{i}\033[m", end=" ")

if cont == 2:
    print(f"\nO numero {num} foi divisivel {cont} vezes.")
    print(f"Logo o numero {num} é primo.")
else:
    print(f"\nO numero {num} foi divisivel {cont} vezes.")
    print(f"Logo o numero {num} não é primo.")

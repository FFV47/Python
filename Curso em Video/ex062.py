print("\033[34m+\033[m" * 60)
print(f"\033[32m {'Progressão Aritmética em While':^60} \033[m")
print("\033[34m=\033[m" * 60)

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

i = 0
cont = 9

print("10 primeiros termos da PA:", end=" ")

# Primeira Solução

while i <= cont:
    print(
        f"\033[31m{primeiro + razao * i}\033[m -> "
        if i != cont
        else f"\033[31m{ primeiro + razao * i}\033[m",
        end="",
    )

    if i == cont:
        i = -1
        mais_termos = int(
            input(
                "\nDigite quantos termos a mais voce deseja (digite 0 para terminar): "
            )
        )
        cont += mais_termos
        if mais_termos == 0:
            break
    i += 1
print(f"Total de termos apresentados: {cont+1}")

# Segunda Solução
# mais_termos = 1

# while mais_termos != 0:
#     while i <= cont:
#         print(
#             f"\033[31m{primeiro + razao * i}\033[m -> "
#             if i != cont
#             else f"\033[31m{primeiro + razao * i}\033[m",
#             end="",
#         )
#         i += 1
#     mais_termos = int(
#         input("\nDigite quantos termos a mais voce deseja (digite 0 para terminar): ")
#     )
#     i = 0
#     cont += mais_termos

# print(f"Total de termos apresentados: {cont+1}")

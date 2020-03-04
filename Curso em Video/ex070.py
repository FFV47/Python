print(f"\033[32m {'Registrador de Produtos':^60} \033[m")
print("\033[34m+\033[m" * 60)

menor = mais1000 = cont = total = 0

while True:

    print(f"{' INFORMAÇÕES DO PRODUTO ':=^60}")
    nome = str(input("Digite o nome do produto: ")).strip()
    preco = int(input("Digite o preço do produto: R$ "))
    opcao = " "

    while opcao not in "SN":
        opcao = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]

    if cont == 0:
        menor = preco

    total += preco
    cont += 1

    if preco > 1000:
        mais1000 += 1

    if preco < menor:
        menor = preco
        barato = nome

    if opcao == "N":
        break

print("-" * 60)
print(f"{'RESUMO DA NOTA FISCAL':^60}")
print("-" * 60)

print(f"Total das Compras: R$ {total:.2f}")
print(f"Quantidade de produtos acimas de R$ 1000,00: {mais1000}")
print(f"Produto mais barato da compra: {barato.upper()}")

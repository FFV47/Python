lista = ()
tam_lista = int(input("Digite a quantidade de itens da lista de compras: "))
for c in range(tam_lista):
    lista += (str(input("Digite o nome do produto: ")),)
    lista += (float(input("Digite o preço do produto: ")),)

soma = sum(lista[1::2])
print("-" * 60)
print(f"\033[31m{'LISTAGEM DE PREÇOS':^60}\033[m")
print("-" * 60)
for i in range(0, len(lista), 2):
    print(f"\033[34m{lista[i]:.<60}\033[m", end="")
    print(f"\033[1;36mR$\033[m \033[1;32m{lista[i+1]:>6.2f}\033[m")

print(f"\033[34m{'Total':.<60}\033[m", end="")
print(f"\033[1;36mR$\033[m \033[1;32m{soma:>6.2f}\033[m")
print("-" * 60)

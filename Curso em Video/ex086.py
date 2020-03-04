tam = int(input("Digite uma tamanho para a matriz: "))
matriz = [[] for i in range(tam)]

print("-=" * 40)
for lin in range(tam):
    for col in range(tam):
        n = int(input(f"Digite um valor para a posição [{lin}, {col}]: "))
        matriz[lin].append(n)

print("-" * 60)

for lin in matriz:
    for col in lin:
        print(f"[{col:^7}]", end="")
    print()
